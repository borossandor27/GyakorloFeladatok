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


def helyreallitas():
    for nap in range(1, 12):
        adasSzoveg = list("#" * 90)
        for i in range(0, 90):
            for adas in uzenetek:
                if adas.nap == nap and adas.uzenet[i] not in "#":
                    adasSzoveg[i] = adas.uzenet[i]
        helyreallitottUzenetek.append(
            HelyreallitottMegfigyeles(nap, "".join(adasSzoveg).replace("$", ""))
        )
    for uzenet in helyreallitottUzenetek:
        print(f"{uzenet.nap:3.0f}. nap - {uzenet.adasSzoveg}")

def f02():
    print("\n2. feladat:")
    print(f"\tAz első üzenet rögzítője: {uzenetek[0].radioAmator}")
    print(f"\tAz utolsó üzenet rögzítője: {uzenetek[len(uzenetek)-1].radioAmator}")
beolvas()
helyreallitas()
f02()
print("\nProgram vége!")
