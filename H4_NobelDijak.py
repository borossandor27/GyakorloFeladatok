class Nobeldij:
    def __init__(self, sor):
        items=sor.strip().split(';')
        self.evszam = int(items[0])
        self.tipus=items[1]
        self.keresztnev=items[2]
        self.vezeteknev=items[3]

kiosztottNobelDijak=[]


def beolvas():
    f = open("forrasok\\nobel.csv", encoding="UTF-8")
    f.readline() # fejlécet átlépjük, eldobjuk
    for sor in f:
        kiosztottNobelDijak.append(Nobeldij(sor))
def f001():
    # Határozza meg és írja ki a képernyőre a minta szerint, hogy Arthur B. McDonald milyen típusú díjat kapott! 
    # Feltételezheti, hogy életében csak egyszer kapott Nobeldíjat
    print("\n1. feladat:")
    for dijazott in kiosztottNobelDijak:
        if dijazott.keresztnev == "Arthur B." and dijazott.vezeteknev == "McDonald":
            print(f"\t{dijazott.keresztnev} {dijazott.vezeteknev} {dijazott.tipus} típusú díjat kapott a {dijazott.evszam}. évben\n")
            break
def f002():
    # Határozza meg és írja ki a képernyőre a minta szerint, hogy ki kapott 2017-ben irodalmi Nobel-díjat!
    print("\n2. feladat:")
    for dijazott in kiosztottNobelDijak:
        if dijazott.evszam == 2017 and dijazott.tipus == "irodalmi":
            print(f"\t{dijazott.keresztnev} {dijazott.vezeteknev} kapott a {dijazott.evszam}. évben {dijazott.tipus} Nobel-díjat\n")
            break
def f003():
    # A Curie család több tagja is kapott díjat. 
    # Határozza meg és írja ki a képernyőre a minta szerint, hogy melyik évben a család melyik tagja milyen díjat kapott!
    print("\n3. feladat:")
    for dijazott in kiosztottNobelDijak:
        if dijazott.vezeteknev.find("Curie") >= 0:
            print(f"\t{dijazott.evszam}. évben {dijazott.keresztnev} {dijazott.vezeteknev} kapott a {dijazott.tipus} Nobel-díjat")
    print("\n")
beolvas()
f001()
f002()
f003()