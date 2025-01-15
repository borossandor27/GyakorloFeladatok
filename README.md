# Gyakorló feladatok 

A ```Programozas_feladatok.pdf```-ben olyan egyszerű feladatok vannak, amelyek
bármelyik programozási nyelv megismeréséhez használhatóak. ***Adatbekérés, értékadások, ...***

A további feladatok a már megismert nyelv rutin szerű gyakorlására alkalmasak. Régebbi OKJ-s és érettségi feladatok programozási feladatai.

## [***f00*** Kéktúra ](./f00_kektura/)
Az Országos Kéktúra Magyarország északi részén végighaladó folyamatos, jelzett
turistaút. A Kéktúrának a Balaton-Felvidéken is több, rövidebb idő alatt bejárható túrája van. Egy ilyen túra adatait kell feldolgoznia ebben a feladatban.
- ```kektura.csv``` állomány beolvasása után egyszerű kimutatások készgítése

## [***f01*** Farkas expedíció](./f01_farkasexpedicio/)
Valamikor a távközlés hőskorában egy ritka farkasfaj tudományos megfigyelésére
expedíciót szerveztek a sarkkörön túlra. A magukkal vitt rádió csak napi egy adásra volt alkalmas, arra is csak 90 időegységig, időegységenként egy karaktert továbbítva.
Az expedíció rádiósának üzeneteit több rádióamatőr is igyekezett lejegyezni. A feladatban a rádióamatőrök által lejegyzett üzeneteket kell feldolgoznia.
A ```veetel.txt``` fájl tartalmazza a rádióamatőrök által feljegyzett üzeneteket.

## [***f02*** Ötszáz](./f02_penztar/) 
Egy apróságokat árusító boltban minden árucikk darabja 500 Ft. Ha egy vásárlás során
valaki egy adott árucikkből több darabot is vesz, a második ára már csak 450 Ft, a harmadik pedig 400 Ft, de a negyedik és további darabok is ennyibe kerülnek, tehát az ár a harmadik ugyanazon cikk vásárlása után már nem csökken tovább.

## [***f03*** Tesztverseny](./f03_tesztverseny/)
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
## ***f13*** Négyzetgyökök keresése 13 pont
A következő algoritmus számok négyzetgyökét határozza meg. Kódolja az algoritmust a
választott programozási nyelven! A ”/*” és ”*/” karakterpárok között megjegyzéseket talál, ezeket helyezze el a megoldásban is! Az elkészült program forráskódját mentse ```Ngyok``` néven!
A megoldás során vegye figyelembe a következőket:
- A választott programozási nyelvtől függően eltérő jelölésű operátorokat és függvényeket
kell alkalmaznia!
- A ”Térj vissza” utasítás megszakítja a függvény futását és meghatározza annak
visszatérési értékét!
- A valós típusú változókhoz használja a legnagyobb pontosságot biztosító adattípust!
- A függvény negatív értékű aktuális paraméter esetén hibakóddal (-1) tér vissza!

```plaintext
Függvény Negyzetgyok(x:Valós): Valós
    Változó pontossag, also, felso, proba: Valós
    /* A legnagyobb pontosságú valós típust használja! */
    Ha x>0 akkor
        pontossag := 0.00000000000001
        Ha x<1 akkor
            also := x
            felso := 1
        különben
            also := 1
            felso := x
        Elágazás vége
        Ciklus amíg (felso – also) > pontossag
            proba := (also + felso) / 2
            Ha proba * proba > x akkor
                felso := proba
            különben
                also := proba
            Elágazás vége
        Ciklus vége
        Térj vissza (also + felso) / 2
    különben
        Ha x=0 akkor
            Térj vissza 0
        különben
            Térj vissza -1
        Elágazás vége
    Elágazás vége
Függvény vége

Program Ngyok:
    Ki: Negyzetgyok(0)
    Ki: Negyzetgyok(3.3)
    Ki: Negyzetgyok(2)
    Ki: Negyzetgyok(9)
    Ki: Negyzetgyok(-9)
Program vége.
```
## ***f14*** Robotvezérlés 
Ebben a feladatban tanulók által írt robotvezérlő kódsorozatokat kell elemeznie. Az elemzésre azért van szükségünk, hogy a tényleges kipróbálás előtt kiszűrjük a hibákat tartalmazó munkákat.

## ***f15*** PI kalkuláció
A következő algoritmus a PI közelítő értékét határozza meg a Spigot algoritmus felhasználásával.
Kódolja az algoritmust a választott programozási nyelven! Az elkészült program forráskódját
mentse Spigot néven!
A megoldás során vegye figyelembe a következőket:
- A választott programozási nyelvtől függően eltérő jelölésű operátorokat és függvényeket
kell alkalmaznia.
- A ”mod” a maradékképzés, a ”div” az egészosztás operátora.
- A ”Térj vissza” utasítás megszakítja a függvény futását és meghatározza annak
visszatérési értékét.
- Az egész típusú változókhoz használjon 32 bites előjeles adattípust!

```plaintext
Függvény SpigotPi(digits: Egész): Szöveg
    Változó N, i, j, q, carry, num: Egész
    Változó result: Szöveg
    N := digits * 3 + 2
    Változó x:Tömb[0..N-1] Egész
    Változó r:Tömb[0..N-1] Egész
    result := ””
    Ciklus j:=0-tól N-1 -ig (+1 lépésközzel)
        x[j] := 20
    Ciklus vége
    Ciklus i:=0-tól digits-1 -ig (+1 lépésközzel)
        carry := 0
        Ciklus j:=0-tól N-1 -ig (+1 lépésközzel)
            x[j] : = x[j] + carry
            num := N - j – 1
            q := x[j] div (num * 2 + 1)
            r[j] := x[j] mod (num * 2 + 1)
            carry := q * num
        Ciklus vége
        Ha (i < digits -1) akkor
            result := result + x[N-1] div 10
        Elágazás vége
        r[N – 1] := x[N-1] mod 10
        Ciklus j:=0-tól N-1 -ig (+1 lépésközzel)
            x[j] := r[j] * 10
        Ciklus vége
    Ciklus vége
    Térj vissza result
Függvény vége
Program Spigot
    Ki: SpigotPi(15)
Program vége
```

## ***f16*** Számsorozat
A következő feladatban egy számsorozat feldolgozásához és elemzéséhez kell programot
készítenie.

## ***f17*** Helsinki 1952 
Az 1952-ben Helsinkiben rendezett nyári olimpián nagyon szépen szerepeltek a
magyar színekben induló olimpikonok. Ebben a feladatban az általuk elért helyezésekkel
kapcsolatos számításokat kell elvégeznie.

## ***f18*** Egyszámjáték
Az egyszámjáték Mérő László matematikus találmánya. A játék nagyon egyszerű.
Mindenkinek, aki a játék egy fordulójában részt kíván venni, tippelnie kell egy számra 1 és
99 között. A játékot az nyeri, aki a legkisebb olyan számra tippelt, amelyre csak ő tippelt
egyedül, ha nincs ilyen szám, akkor a fordulónak nincs nyertese.
Ebben a feladatban egy többfordulós egyszámjátékkal kapcsolatban kell feladatokat
megoldania.

## ***f19*** Footgolf
A footgolf egy szabadtéri sport, melynek fő célja, hogy egy futball-labdát a lehető
legkevesebb számú rúgással eljuttassunk az elrúgóhelynek kijelölt lapos területről a pálya
végén található lyukba. A játék szabályainak alapjait a golf sportág adja, míg a technikai
tudás a futball során sajátítható el. A magyar bajnokságban nyolc fordulóban mérik össze
tudásukat az indulók. A versenyzők fordulónkénti pontszáma a helyezésért járó pontból és a
versenyen indulásért kapott bónuszpontból (10 pont) tevődik össze. Ebben a feladatban a
2016-os footgolf országos bajnokság adataival kell feladatokat megoldania.

## ***f20*** Üzemanyagárak változása
Az üzemanyagok (benzin és gázolaj) fogyasztói ára gyakran hetenként változik. Ebben a
feladatban a 2011-2016-os időszak átlagos árainak változásaival kell feladatokat megoldania.

