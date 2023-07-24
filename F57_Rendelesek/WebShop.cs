using System;
using System.Collections.Generic;
using System.IO;

namespace Webshop
{
    class WebShop
    {
        static List<Raktar> raktar = new List<Raktar>();
        static List<Rendeles> rendelesek = new List<Rendeles>();

        static void Main(string[] args)
        {
            Console.WriteLine("Web Shop");
            Console.WriteLine("\n1. feladat:");
            RatarAdatokBeolvasasa();
            MegrendelesAdatokBeolvasasa();
            Console.WriteLine("\n2. feladat:");
            RendelesFeldolgozas();
            Console.WriteLine("\n3. feladat:");
            LevelKeszites();
            Console.WriteLine("\n4. feladat:");
            BeszerzesKeszites();
            Console.WriteLine("\n\nProgram vége!\n\n\nKilépés bármely billentyű leütésére...");
            Console.ReadKey();
        }

        static void RatarAdatokBeolvasasa()
        {
            Console.WriteLine("\tRaktár adatok beolvasása...");
            using (StreamReader sr=new StreamReader("raktar.csv"))
            {
                while (!sr.EndOfStream)
                {
                    raktar.Add(new Raktar(sr.ReadLine()));
                }
                sr.Close();
            }
        }

        static void MegrendelesAdatokBeolvasasa()
        {
            Console.WriteLine("\tMegrendelés adatok beolvasása...");
            using (StreamReader sr = new StreamReader("rendeles.csv"))
            {
                int RendelesSzam = -1;
                while (!sr.EndOfStream)
                {
                    string[] ujSor = sr.ReadLine().Split(";");
                    if (ujSor[0]=="M")
                    {
                        RendelesSzam++;
                        rendelesek.Add(new Rendeles(ujSor));
                    }
                    else if (ujSor[0]=="T")
                    {
                        rendelesek[RendelesSzam].UjTetel(ujSor);
                    }
                }
                sr.Close();
            }
        }

        static void RendelesFeldolgozas()
        {
            Console.WriteLine("\tRendelési adatok feldolgozása...");
            //-- A rendelés teljesíthetőségének a vizsgálata
            foreach (Rendeles item in rendelesek)
            {
                item.Teljesitheto = true;
                for (int i = 0; i < item.Tetelek.Count; i++)
                {
                    string tk = item.Tetelek[i].TermekKod;
                    int rendelve = item.Tetelek[i].Mennyiseg;
                    int raktarKeszlet = raktar.Find(x => x.TermekKod == tk).TermekKeszlet;
                    if (raktarKeszlet < rendelve)
                    {
                        item.Teljesitheto = false;
                        break;
                    }
                }
            }
            //-- Készlet csokkentése, ha teljesíthető
            Console.WriteLine("\tKészletcsökkentés...");
            foreach (Rendeles item in rendelesek)
            {
                if (item.Teljesitheto)
                {
                    for (int i = 0; i < item.Tetelek.Count; i++)
                    {
                        string tk = item.Tetelek[i].TermekKod;
                        int rendelve = item.Tetelek[i].Mennyiseg;
                        int raktarKeszlet = raktar.Find(x => x.TermekKod == tk).TermekKeszlet;
                        raktar.Find(x => x.TermekKod == tk).TermekKeszlet = raktarKeszlet - rendelve;
                    }
                }
            }
        }

        static void LevelKeszites()
        {
            Console.WriteLine("\tlevel.csv állomány kiirasa...");
            using (StreamWriter sw = new StreamWriter("levelek.csv"))
            {
                foreach (Rendeles item in rendelesek)
                {
                    if (item.Teljesitheto)
                    {
                        //-- Az összeg meghatározása
                        for (int i = 0; i < item.Tetelek.Count; i++)
                        {
                            item.RendelesErteke += raktar.Find(x => x.TermekKod == item.Tetelek[i].TermekKod).TermekAr;
                        }
                        sw.WriteLine("{0};A rendelését két napon belül szállítjuk. A rendelés értéke: {1} Ft", item.emailCim, item.RendelesErteke);
                    }
                    else
                    {
                        sw.WriteLine("{0};A rendelése függő állapotba került. Hamarosan értesítjük a szállítás időpontjáról.", item.emailCim);
                    }
                }
                sw.Close();
            }
        }

        static void BeszerzesKeszites()
        {
            List<BeszerzesAdat> beszerzes = new List<BeszerzesAdat>();
            //-- A rendelésekből kigyűjtjük a "várakozó" tételek darabszámait
            foreach (Rendeles item in rendelesek)
            {
                if (!item.Teljesitheto)
                {
                    for (int i = 0; i < item.Tetelek.Count; i++)
                    {
                        if (beszerzes.Exists(x => x.Termekkod == item.Tetelek[i].TermekKod))
                        {
                            beszerzes.FindAll(x => x.Termekkod == item.Tetelek[i].TermekKod).ForEach(x => x.Mennyiseg += item.Tetelek[i].Mennyiseg);
                        }
                        else
                        {
                            beszerzes.Add(new BeszerzesAdat(item.Tetelek[i].TermekKod, item.Tetelek[i].Mennyiseg));
                        }
                    }
                }
            }
            //-- Kigyűjtött adatokat fájlba írjuk
            using (StreamWriter sw = new StreamWriter("beszerzes.csv"))
            {
                foreach (BeszerzesAdat item in beszerzes)
                {
                    sw.WriteLine("{0};{1}", item.Termekkod, item.Mennyiseg);
                }
                sw.Close();
            }
        }
    }


    class Raktar
    {
        public string TermekKod;
        public string TermekNev;
        public int TermekAr;
        public int TermekKeszlet;

        public Raktar(string line)
        {
            string[] uj = line.Split(";");
            TermekKod = uj[0];
            TermekNev = uj[1];
            TermekAr = int.Parse(uj[2]);
            TermekKeszlet = int.Parse(uj[3]);
        }
    }

    class RendelesTetel
    {
        public string TermekKod;
        public int Mennyiseg;

        public RendelesTetel(string[] uj)
        {
            TermekKod = uj[2];
            Mennyiseg = int.Parse(uj[3]);
        }
    }

    class Rendeles
    {
        public int RendelesSzam;
        public DateTime RendelesDatum;
        public string emailCim;
        public bool Teljesitheto = false;
        public int RendelesErteke = 0; //-- a 3. feladat miatt
        public List<RendelesTetel> Tetelek = new List<RendelesTetel>();

        public Rendeles(string[] uj)
        {
            RendelesDatum = DateTime.Parse(uj[1]);
            RendelesSzam = int.Parse(uj[2]);
            emailCim = uj[3];
        }

        public void UjTetel(string[] uj)
        {
            Tetelek.Add(new RendelesTetel(uj));
        }

    }

    class BeszerzesAdat
    {
        public string Termekkod;
        public int Mennyiseg;
        public BeszerzesAdat(string kod, int db)
        {
            Termekkod = kod;
            Mennyiseg = db;
        }
    }
}
