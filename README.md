# Az INFORMATIKA ÉS TÁVKÖZLÉS ágazathoz tartozó 
- 5 0613 12 03 SZOFTVERFEJLESZTŐ ÉS –TESZTELŐ SZAKMA
- 5 0612 12 02INFORMATIKAI RENDSZER- ÉS ALKALMAZÁSÜZEMELTETŐ TECHNIKUS SZAKMA

ágazati alapvizsga python vizsgájára felkészítő egyszerű feladatok,
de bármelyik programozási nyelv megismeréséhez használhatóak

A python megoldások: https://github.com/borossandor27/pythonGyakorloFeladatok.git

A megoldások nem a nyelv szépségét kívánják bemutatni, nem használják ki az összes nyelvi lehetőséget, hanem a sikeres vizsgához szükséges ismereteket próbálják bemutatni

## ***f00*** Kéktúra 
Az Országos Kéktúra Magyarország északi részén végighaladó folyamatos, jelzett
turistaút. A Kéktúrának a Balaton-Felvidéken is több, rövidebb idő alatt bejárható túrája van. Egy ilyen túra adatait kell feldolgoznia ebben a feladatban.
- ```kektura.csv``` állomány beolvasása után egyszerű kimutatások készítése

## ***f01*** Expedíció 
Valamikor a távközlés hőskorában egy ritka farkasfaj tudományos megfigyelésére
expedíciót szerveztek a sarkkörön túlra. A magukkal vitt rádió csak napi egy adásra volt alkalmas, arra is csak 90 időegységig, időegységenként egy karaktert továbbítva.
Az expedíció rádiósának üzeneteit több rádióamatőr is igyekezett lejegyezni. A feladatban a rádióamatőrök által lejegyzett üzeneteket kell feldolgoznia.
A ```veetel.txt``` fájl tartalmazza a rádióamatőrök által feljegyzett üzeneteket.

## ***f02*** Ötszáz 
Egy apróságokat árusító boltban minden árucikk darabja 500 Ft. Ha egy vásárlás során
valaki egy adott árucikkből több darabot is vesz, a második ára már csak 450 Ft, a harmadik pedig 400 Ft, de a negyedik és további darabok is ennyibe kerülnek, tehát az ár a harmadik ugyanazon cikk vásárlása után már nem csökken tovább.

## ***f03*** Tesztverseny 
Egy közismereti versenyen a versenyzőknek 13+1, azaz összesen 14 tesztfeladatot tűznek ki. A versenyzőknek minden feladat esetén négy megadott lehetőség (A, B, C, D) közül kell a helyes választ megjelölniük. A versenybizottság garantálja, hogy tesztlapon minden kérdéshez pontosan egy helyes válasz tartozik. A kitöltött tesztlapokat elektronikusan rögzítik, a visszaélések elkerülése végett a versenyzőket betűkből és számokból álló kóddal azonosítják.

## ***f04*** Társalgó
Egy színház társalgójában még a délelőtti próbák alatt is nagy a forgalom. A színészek hosszabb-rövidebb beszélgetésekre térnek be ide, vagy éppen csak keresnek valakit. A feladatban a társalgó ajtajánál 9 és 15 óra között felvett adatokat kell feldolgoznia.

## ***f05*** Levenshtein-távolság
A következő algoritmus két, maximum 25 karakter hosszú karakterláncról megállapítja,
hogy mekkora a Levenshtein-távolságuk, azaz minimálisan hány karakterenkénti művelet
(beszúrás, törlés, csere) kell ahhoz, hogy az egyik karakterláncot a másikra átalakítsuk. Kódolja az algoritmust a választott programozási nyelven! 

## ***f06*** Pontok 
Ebben a feladatban egy szöveges állományban x, y koordinátákkal megadott pontokat kell vizsgálnia. Minden pont adata külön sorba került a forrásállományban a sorszámuk
alapján...

## ***f07*** Shell rendezés
A következő algoritmus a Shell rendezés algoritmusával rendezi az N elemű (N<100)
vektorban megadott számokat növekvő sorrendben.
Kódolja az algoritmust a választott programozási nyelven! Az elkészült program
forráskódját mentse shellsort néven!

A megoldás során vegye figyelembe a következőket:
- A választott programozási nyelvtől függően eltérő jelölésű operátorokat,
adattípusokat és függvényeket kell alkalmaznia.
- A ”div” az egészosztás operátora.
- Az egész típusú változókhoz és vektorokhoz használjon 32 bites előjeles adattípust!

```plaintext
Eljárás ShellRendezes(a:Tömb[0..N] Egész)
    Változó gap, n, i, j, x, y : Egész
    gap := 1
    n := a.Hossz //a vektor elemszáma
    Ciklus amíg (gap * 2 <= n)
        gap := gap * 2
    Ciklus vége
    gap := gap - 1
    Ciklus
        i := 0
        Ciklus amíg ((i <= gap) ÉS (i + gap < n))
            j := i + gap
            Ciklus amíg (j < n)
                x := a[j]
                y := j – gap
                Ciklus amíg ((x > -1) ÉS (x < a[y]))
                    a[y + gap] := a[y]
                    y := y – gap
                Ciklus vége
                a[y + gap] := x
                j := j + gap
            Ciklus vége
            i := i + 1
        Ciklus vége
        gap := gap div 2
    amíg (gap > 0)
    Ciklus vége
Eljárás vége

Program shellsort
    Változó t: Tömb[0..9] Egész
    t[0] := 63
    t[1] := 54
    t[2] := 33
    t[3] := 45
    t[4] := 23
    t[5] := 99
    t[6] := 43
    t[7] := 10
    t[8] := 35
    t[9] := 87
    ShellRendezes(t)
    Ciklus i:=0 -tól 9 –ig (+1 lépésközzel)
        Ki: t[i]
    Ciklus vége
Program vége
```

## ***f08*** Bástyák
Ebben a feladatban egy 8x8-as mátrixban mint sakktáblán a számítógép által
véletlenszerűen elhelyezett bástyákkal és gyalogokkal fog dolgozni.

## ***f09*** Reversi 
A reversi játékot általában 8×8 mezőből álló négyzetrácsos táblán játsszák. Ebben a
feladatban a tábla sorait és oszlopait is 0-tól 7-ig azonosítjuk az ábra szerint. A játékot legjobb olyan korongokkal játszani, amelyek két oldala különböző színű (feladatunkban kék és fehér). A két játékos felváltva rakja le korongjait. ...

## ***f10*** Lézerlövészet 
Egy baráti társaságban népszerű szórakozás a lézerlövészet, ahol a játékosok elektronikus fegyverrel lőnek virtuális céltáblára. Mivel csak egy fegyverük van, így minden lövés előtt kockadobással határozzák meg a soron következő játékost. A kockadobásban mindenki részt vesz, így egymás után akár több lövést is leadhat egy-egy játékos.

## ***f11*** kő-papír-olló
Írjon programot a kő-papír-olló játékkal kapcsolatos feladatok megoldására! A program olvassa be két játékos választását kódok segítségével a minta szerint, majd tárolja azokat! 

## ***f12*** koktélrendezés
Kódolja az alábbi algoritmust a választott programozási nyelven!
Az algoritmus egy bájt típusú, 10 elemű vektort rendez növekvő sorrendben a koktélrendezés módszerével.
```plaintext
Eljárás KiirTomb(t:Egész elemű tömb)
    Ciklus i=0-tól t.Hossz-1-ig (+1 lépésközzel)
        Ki: t[i],”, ”
    Ciklus vége
    Ki: Soremelés [CR és LF vezérlőkarakterek]
Eljárás vége

Program:
    Változó tömb t[0..9]:Egész = {54,68,14,70,93,91,39,37,7,13}
    Változó kezd:Egész = 0
    Változó veg:Egész = t.Hossz - 1
    Változó csereVolt:Logikai
    Változó csere:Egész
    KiirTomb(t)
    Ciklus
        csereVolt = Hamis
        Ciklus i=kezd-tól veg-1 -ig (+1 lépésközzel)
            Ha t[i] > t[i + 1]
            akkor
            csere = t[i]
            t[i] = t[i + 1]
            t[i + 1] = csere
            csereVolt = Igaz
            Elágazás vége
        Ciklus vége
        veg = veg – 1
        Ha csereVolt=Igaz
        akkor
            csereVolt = Hamis
            Ciklus i=veg-től kezd+1 -ig (-1 lépésközzel)
                Ha t[i] < t[i - 1]
                akkor
                    csere = t[i]
                    t[i] = t[i - 1]
                    t[i - 1] = csere
                    csereVolt = Igaz
                Elágazás vége
            Ciklus vége
            kezd = kezd + 1
        Elágazás vége
    amíg csereVolt = Igaz
    KiirTomb(t)
Program vége.
```
