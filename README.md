# Gyakorló feladatok 

A [```Programozas_feladatok.pdf```](./Programozas_feladatok.pdf)-ben olyan egyszerű feladatok vannak, amelyek
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

## [***f04*** Társalgó](./f04_tarsalgo/)
Egy színház társalgójában még a délelőtti próbák alatt is nagy a forgalom. A színészek hosszabb-rövidebb beszélgetésekre térnek be ide, vagy éppen csak keresnek valakit. A feladatban a társalgó ajtajánál 9 és 15 óra között felvett adatokat kell feldolgoznia.

## [***f05*** Levenshtein-távolság](./f05_Levenshtein_tavolsag/)
A következő algoritmus két, maximum 25 karakter hosszú karakterláncról megállapítja,
hogy mekkora a Levenshtein-távolságuk, azaz minimálisan hány karakterenkénti művelet
(beszúrás, törlés, csere) kell ahhoz, hogy az egyik karakterláncot a másikra átalakítsuk. Kódolja az algoritmust a választott programozási nyelven! 

## [***f06*** Pontok](./f06_pontok/)
Ebben a feladatban egy szöveges állományban x, y koordinátákkal megadott pontokat kell vizsgálnia. Minden pont adata külön sorba került a forrásállományban a sorszámuk
alapján...

## [***f07*** Shell rendezés](./f07_Shell-rendezes/)
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

## [***f08*** Bástyák](./f08_bastyak/)
Ebben a feladatban egy 8x8-as mátrixban mint sakktáblán a számítógép által
véletlenszerűen elhelyezett bástyákkal és gyalogokkal fog dolgozni.

## [***f09*** Reversi](./f09_reversi/) 
A reversi játékot általában 8×8 mezőből álló négyzetrácsos táblán játsszák. Ebben a
feladatban a tábla sorait és oszlopait is 0-tól 7-ig azonosítjuk az ábra szerint. A játékot legjobb olyan korongokkal játszani, amelyek két oldala különböző színű (feladatunkban kék és fehér). A két játékos felváltva rakja le korongjait. ...

## [***f10*** Lézerlövészet](./f10_lezerloveszet/)
Egy baráti társaságban népszerű szórakozás a lézerlövészet, ahol a játékosok elektronikus fegyverrel lőnek virtuális céltáblára. Mivel csak egy fegyverük van, így minden lövés előtt kockadobással határozzák meg a soron következő játékost. A kockadobásban mindenki részt vesz, így egymás után akár több lövést is leadhat egy-egy játékos.

## [***f11*** kő-papír-olló](./f11_koPapirOllo/)
Írjon programot a kő-papír-olló játékkal kapcsolatos feladatok megoldására! A program olvassa be két játékos választását kódok segítségével a minta szerint, majd tárolja azokat! 

## [***f12*** koktélrendezés](./f12_koktelrendezes/)
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
## [***f13*** Négyzetgyökök keresése](./f13_negyzetgyokok/)
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
## [***f14*** Robotvezérlés](./f14_robotvezerles/)
Ebben a feladatban tanulók által írt robotvezérlő kódsorozatokat kell elemeznie. Az elemzésre azért van szükségünk, hogy a tényleges kipróbálás előtt kiszűrjük a hibákat tartalmazó munkákat.

## [***f15*** PI kalkuláció](./f15_SpigotPi/)
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

## [***f16*** Számsorozat](./f16_szamsorozat/)
A következő feladatban egy számsorozat feldolgozásához és elemzéséhez kell programot
készítenie.

## [***f17*** Helsinki 1952](./f17_helsinki_1952/)
Az 1952-ben Helsinkiben rendezett nyári olimpián nagyon szépen szerepeltek a
magyar színekben induló olimpikonok. Ebben a feladatban az általuk elért helyezésekkel
kapcsolatos számításokat kell elvégeznie.

## [***f18*** Egyszámjáték](./f18_egyszamjatek/)
Az egyszámjáték Mérő László matematikus találmánya. A játék nagyon egyszerű.
Mindenkinek, aki a játék egy fordulójában részt kíván venni, tippelnie kell egy számra 1 és
99 között. A játékot az nyeri, aki a legkisebb olyan számra tippelt, amelyre csak ő tippelt
egyedül, ha nincs ilyen szám, akkor a fordulónak nincs nyertese.
Ebben a feladatban egy többfordulós egyszámjátékkal kapcsolatban kell feladatokat
megoldania.

## [***f19*** Footgolf](./f19_footgolf/)
A footgolf egy szabadtéri sport, melynek fő célja, hogy egy futball-labdát a lehető
legkevesebb számú rúgással eljuttassunk az elrúgóhelynek kijelölt lapos területről a pálya
végén található lyukba. A játék szabályainak alapjait a golf sportág adja, míg a technikai
tudás a futball során sajátítható el. A magyar bajnokságban nyolc fordulóban mérik össze
tudásukat az indulók. A versenyzők fordulónkénti pontszáma a helyezésért járó pontból és a
versenyen indulásért kapott bónuszpontból (10 pont) tevődik össze. Ebben a feladatban a
2016-os footgolf országos bajnokság adataival kell feladatokat megoldania.

## [***f20*** Üzemanyagárak változása](./f20_uzemanyag/)
Az üzemanyagok (benzin és gázolaj) fogyasztói ára gyakran hetenként változik. Ebben a
feladatban a 2011-2016-os időszak átlagos árainak változásaival kell feladatokat megoldania.

## [***f21*** Hegyláncok feladat](./f21_hegylancok/)
A feladatban egy hegymagasságokat tartalmazó adatsorral kell dolgoznia. Az adatsorban a
hegymagasságokat 0−15 közötti véletlenszerűen generált számokkal határozzuk meg. Az
a feladata, hogy a hegymagasságokat tartalmazó adatsort létrehozza és feldolgozza.

## [***f22*** Hiányzások](./f22_hianyzasok/)
Egy osztály második félévi hiányzásai állnak rendelkezésére a naplo.txt fájlban.
A hiányzások naponként csoportosítva szerepelnek, minden napot a # karakter kezd, majd egyegy szóközzel elválasztva a hónap és a nap sorszáma következik. Az aznapi hiányzások
tanulónként külön sorokban vannak, a tanuló napi hiányzásait egy hét karakterből álló
karaktersorozat írja le. A karaktersorozat minden karaktere egy-egy órát ad meg. Értéke
az O betű, ha a tanuló jelen volt az adott órán, az X utal az igazolt, az I az igazolatlan távollétre,
végül N betű jelzi, ha a tanulónak akkor nem volt órája. 

## [***f23*** Kerítés](./F23_kerites/)
Egy üdülőfalu újonnan nyitott utcájában a telkeket a saroktól kiindulva egymás után
folyamatosan, kihagyások nélkül adják el. A vásárló kiválaszthatja az oldalt, amelyen vásárolni
akar (*ott csak a soron következő telket vásárolhatja meg*), valamint megadhatja a telek
utcafronti szélességét. Sok telket vettek meg az utcában, a legtöbben már kerítést is építettek,
azok majd’ mindegyikét be is festették.

A **kerites.txt** fájl az utca telkeinek jelenlegi állapotát írja le. A telkek a vásárlás
sorrendjében szerepelnek. Minden sorban három adat található. Az első szám megadja, hogy a
telek a páros (0) vagy a páratlan (1) oldalán van az utcának; a második a telek szélességét adja
meg méterben (*egész szám, értéke 8 és 20 között lehet*); a harmadik pedig az utcafronti kerítés
színét leíró karakter. A szín az angol ábécé nagybetűje. Ha a kerítést már elkészítették, de nem
festették be, akkor a „#” karakter, ha még nem készült el, akkor a „:” (kettőspont) karakter
szerepel. Az utca hossza legfeljebb 1000 méter. Mindkét oldalon elkelt legalább 3-3 telek.

## [***f26*** Kutyák](./f26_Kutyak/)
Kutyák állatorvosi adatait tartalmazó szövegfájlokkal kell dolgozni

## [***f27*** Lift](./f27_lift/)
A Madárház Kft. toronyházak építésével foglalkozik. Jelenleg a Csúcs Rt. 100 szintes
szerkezetkész épületén kezdték meg a belső szerelési műveleteket. Az egyes szerelőcsapatok
naponta többször változtatják helyüket. Ha az új munkaterület egy másik emeleten van, akkor
– a biztonsági előírások miatt – lifttel kell menniük. A házban egyetlen lift működik, amelynek igénybevételét az egyes csapatok a célszint megadásával jelezhetik. A lift az igényeket a
jelzés sorrendjében szolgálja ki, és egyszerre csak egy csapatot szállít. A csapatok mozgását a
9 és 14 óra közötti intervallumban követjük nyomon. Ez az intervallum a munkaidőnek csak
egy része, tehát a csapatok már dolgoznak valamelyik szinten, de 9 órakor teljesítetlen kérés
nincs és a lift szabad.

## [***f28*** Születések száma Vas megyében](./f28_Szuletesek_Vas_megyeben/)
A következő feladatban több, egész évet felölelő időszakban vizsgáljuk Vas megyében az élve születések számát. A forrásállományba (vas . txt) az itt született csecsemők személyi azonosítója (személyi száma) került (az azonosítók fiktívek). Az azonosítók képzésének a  szabálya 1997. január 1-jétől megváltozott, ezért a forrásállományban csak 1997-es vagy későbbi személyi azonosítók lehetnek. 

## [***f29*** Királynők](./f29_Kiralynok/)
Ebben a feladatban egy 8x8-as mátrixban mint sakktáblán a számítógép által
véletlenszerűen elhelyezett királynőkkel fog dolgozni. A sakktábla sorait és oszlopait 0-
tól 7-ig egész számokkal azonosítjuk.


## [***f31*** Műkorcsolya 2017](./f31_Mukorcsolya_2017/)
A feladat során a 2017-es műkorcsolya- és jégtánc-világbajnokság női egyéni versenyszámának eredményeit kell feldolgoznia. A verseny minden induló számára a rövidprogrammal kezdődik. A versenyzők értékelése során a zsűritől technikai és komponens pontszámokat, valamint hibapontokat kapnak. A rövidprogram összpontszámának kiszámításakor a technikai és a komponens pontszámok összegéből vonják le a hibapontokat.

## [***f32*** Nobel-díjak](./f32_Nobel-dij/)
A következő feladatban a Svéd Királyi Tudományos Akadémia által osztott Nobel-díj napjainkig feljegyzett adatait tartalmazó szöveges állományt kell feldolgoznia. 

## [***f33*** Osztályzatok feladat](./f33_osztalyzatok/)
Tervezze meg és készítse el azt a programot, amely egy osztály osztályzatait kezeli.

## [***f35*** Szín-kép](./f35_Szin-kep/)
Egy digitális kép tárolásánál minden egyes képpont színét tároljuk. A képpontok színét
az RGB kód adja. Az RGB kód a vörös (R), zöld (G) és a kék (B) színösszetevő értékét
határozza meg. Ezen színösszetevők értéke 0 és 255 közötti egész szám lehet.

## [***f36*** Kéktúra](./F36_Kektura/)
Az Országos Kéktúra Magyarország északi részén végighaladó folyamatos, jelzett
turistaút. A Kéktúrának a Balaton-felvidéken is több, rövidebb idő alatt bejárható túrája van.
Egy ilyen túra adatait kell feldolgoznia ebben a feladatban.

## [***f37*** Fehérje](./F37_Feherje_feladat/)
A fehérjék óriás molekulák, amelyeknek egy része az élő szervezetekben végbemenő folyamatokat katalizálják. Egy-egy fehérje aminosavak százaiból épül fel, melyek láncszerűen
kapcsolódnak egymáshoz. A természetben a fehérjék fajtája több millió. Minden fehérje húszféle aminosav különböző mennyiségű és sorrendű összekapcsolódásával épül fel.

## [***f38*** Kugli](./F38_Kugli/)
A kugli játéknál 9 bábut állítanak fel egy négyzet alakú helyre, ezeket a bábukat egy golyóval
lehet ledönteni. A játékosok egymás után dobnak. A játékszabály a következő: a játékosoknak
legalább annyi bábut kell ledöntenie, mint amennyit az előtte dobó játékos ledöntött. Ha
kevesebbet dönt le, akkor hibapontot kap. A játékos 2 hibapont után kiesik a játékból. A
játékosok száma 5, és a játék 4 kör alatt ért véget...

## [***f39*** Lottó](./F39_Lotto_feladat/)
Magyarországon 1957 óta lehet ötös lottót játszani. A játék lényege a következő: a lottószelvényeken 90 szám közül 5 számot kell a fogadónak megjelölnie. Ha ezek közül 2 vagy annál
több megegyezik a kisorsolt számokkal, akkor nyer. Az évek során egyre többen hódoltak
ennek a szerencsejátéknak és a nyeremények is egyre nőttek.

## [***f40*** SMS szavak](./F40_Sms_szavak_feladat/)
Napjainkban a kommunikáció egy elterjedt formája az SMS-küldés. Az SMS-küldésre alkalmas telefonok prediktív szövegbevitellel segítik az üzenetek megírását. Ennek használatakor a szavakat úgy tudjuk beírni, hogy a telefon számbillentyűjén található betűknek megfelelő számokat kell beírnunk.

## [***f41*** Személyazonosító jel](./F41_SzemSzam_feladat/)
Az ország állampolgárainak van egyedi azonosítójuk. Ez a személyazonosító jel. Az 1997. január 1-je után születetteknél ez a következőképpen néz ki...

## [***f42*** Telefonszámla](./F42_Telefonszamla/)
Egy új szolgáltatás keretében ki lehet kérni a napi telefonbeszélgetéseink listáját. A listát egy fájlban küldik meg, amelyben a következő adatok szerepelnek: hívás kezdete, hívás vége, hívott telefonszám. A hívás kezdete és vége óra, perc, másodperc formában szerepel...

## [***f43*** Triatlon](./F43_Triatlon/)
Egy triatlon versenyen a versenyzőknek a verseny folyamán egymás után kell először
úszniuk, kerékpározniuk majd futniuk. Az győz, aki a legrövidebb idő alatt fejezi be a versenyt. Az egyes versenyzők adatai és időeredményei a triatlon.be fájlban találhatók...

## [***f44*** Vigenère tábla](./F44_Vigenere_CS/)
Már a XVI. században komoly titkosítási módszereket találtak ki az üzenetek elrejtésére. A század egyik legjobb kriptográfusának Blaise de Vigenère-nek a módszerét olvashatja a következőkben...

## [***f45*** Zenei adók](./F45_Zenei_adok_CS_Linq_NL/)
A rádióhallgatás ma már egyre inkább zene vagy hírek hallgatására korlátozódik. Ez a feladat három, folyamatosan zenét sugárzó adóról szól, azok egyetlen napi műsorát feldolgozva. A reklám elkerülése érdekében az adókat nevük helyett egyetlen számmal azonosítottuk...

## [***f46*** csudh.edu](./F46_csudh.edu/)
A Kaliforniában található CSUDH Egyetem weboldalának elkészítéséhez kell támogatást nyújtania. Az egyetem weboldalán egy táblázatban szeretné feltüntetni a saját gondozásában lévő szerverek domainneveit és a hozzájuk tartozó IP-címeket, amihez Önnek egy segédprogramot kell elkészítenie...

## [***f47*** DHCP szerver](./F47_DHCP/)
Készítsen programot az alábbi feladatra az Ön által tanult programozási nyelven! Az
elkészítendő programnak egy DHCP szerver működését kell szimulálnia. A DHCP
szerver a 192.168.10.100 – 192.168.10.199-as tartományból osztja az IP-címeket. A
feladathoz négy induló állomány tartozik...

## [***f48*** Az Európai Unió tagállamai](./F48_EU_tagallamok/)
Ebben a feladatban egy programot kell készítenie, amelyben az Európai Unió tagállamaival és a csatlakozási dátumokkal kell dolgoznia...

## [***f49*** Fuvar](./F49_Fuvar/)
A következő feladatban 2016-os chicagói taxis fuvarozások adatait tartalmazó szöveges állományt kell feldolgoznia. A megoldás során vegye figyelembe a következőket...

## [***f50*** Hotellift](./F50_Hotellift/)
A következő feladatban egy Balaton-parti hotel lifthasználatát kell elemeznie egy rövid, előszezoni időszakban. A liftet minden vendég csak a személyes, sorszámozott kártyájával tudja igénybe venni. Az utasok a kártyával történő azonosítás után tudják a liftet az induló szintre hívni és a célnak beírt szintre utazásra használni. A forrásállomány (lift . txt) soraiban időrendben egy-egy lifthasználat adatait rögzítettük. Egy sorban rendre a követketó adatok találhatók: használat időpontja, kártya sorszáma, az induló- és a célszint sorszáma. Az adatokat szóköz karakterrel választottuk el egymástól. A megoldás során vegye figyelembe a következőket...
