import os

sor = 0


class Megfigyeles:
    def __init__(self, elsosor, masodiksor):
        global sor
        sor = sor + 1
        items = elsosor.strip().split(" ")
        self.nap = int(items[0])
        self.radioAmator = int(items[1])
        self.uzenet = masodiksor


class HelyreallitottMegfigyeles:
    def __init__(self, nap, adasSzoveg):
        self.nap = nap
        self.adasSzoveg = adasSzoveg

    def __str__(self):
        return self.nap + " - " + self.adasSzoveg + "\n"


os.system("cls")
uzenetek = []
helyreallitottUzenetek = []


def beolvas():
    file = open("veetel.txt")
    for sor in file:
        uzenetek.append(Megfigyeles(sor, file.readline()))


def f02():
    print("\n2. feladat:")
    print(f"\tAz első üzenet rögzítője: {uzenetek[0].radioAmator}")
    print(f"\tAz utolsó üzenet rögzítője: {uzenetek[len(uzenetek)-1].radioAmator}")


def f03():
    # Adja meg az összes olyan feljegyzés napját és a rádióamatőr sorszámát,
    # amelynek szövegében a „farkas” karaktersorozat szerepel!
    print("\n3. feladat:")
    for uzenet in uzenetek:
        if "farkas" in uzenet.uzenet:
            print(f"\t{uzenet.nap:2.0f}. nap {uzenet.radioAmator}. rádióamatőr")


def f04():
    # Készítsen statisztikát, amely megadja, hogy melyik napon hány rádióamatőr készített feljegyzést.
    # Azok a napok 0 értékkel szerepeljenek, amikor nem született feljegyzés!
    # Az eredmény a képernyőn jelenjen meg a napok sorszáma szerint növekvően!
    # A megjelenítést a feladat végén látható minta szerint alakítsa ki!
    print("\n4. feladat:")
    for nap in range(1, 12):
        count = 0
        for uzenet in uzenetek:
            if nap == uzenet.nap:
                count += 1
        print(f"\t{nap:2.0f}. nap {count} rádióamatőr")


def f05():
    # üzenetek heyreállítása
    print("\n5. feladat: üzenetek helyreállítása...")
    for nap in range(1, 12):
        adasSzoveg = list("#" * 90)
        for i in range(0, 90):
            for adas in uzenetek:
                if adas.nap == nap and adas.uzenet[i] not in "#":
                    adasSzoveg[i] = adas.uzenet[i]
        helyreallitottUzenetek.append(
            HelyreallitottMegfigyeles(nap, "".join(adasSzoveg).replace("$", ""))
        )
    file = open("adaas.txt", "w")
    for uzenet in helyreallitottUzenetek:
        # print(f"{uzenet.nap:3.0f}. nap - {uzenet.adasSzoveg}")
        file.writelines(f"{uzenet.nap:3.0f}. nap - {uzenet.adasSzoveg}\n")


def f07():
    #
    nap = int(input("Kérem a nap sorszámát (1-11): "))
    radios = int(input("Kérem a rádióamatőr sorszámát (1-20): "))
    adas = None
    for uzenet in uzenetek:
        if uzenet.nap == nap and radios == uzenet.radioAmator:
            adas = uzenet.uzenet
    if adas==None:
        print("Nincs ilyen feljegyzés")
    elif adas[0].isdigit():
        megfigyeles = adas.split(" ")[0]
        if "#" in megfigyeles:
            print("Nem megállapítható")
        elif "/" in megfigyeles:
            egyedek = megfigyeles.split("/")
            felnott = int(egyedek[0])
            kolyok = int(egyedek[1])
            print(f"A megfigyelt egyedek száma: {felnott+kolyok}")
    else:
        print("Nincs információ")


beolvas()
f02()
f03()
f04()
f05()
f07()
print("\nProgram vége!")
