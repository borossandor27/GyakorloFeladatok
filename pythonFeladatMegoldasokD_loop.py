"""
Iterációk
"""
import random, os

os.system("cls")


def f001_for():
    # kiírja 10 és 20 között az egész számokat.
    # elöltesztelős, határozott lépésszámú
    for i in range(10, 21):
        print(i)
    else:
        print("\nProgram vége!")


def f001_while():
    # kiírja 10 és 20 között az egész számokat.
    # elöltesztelős, határozatlan lépésszámú
    szam = 10
    while szam < 21:
        print(szam)
        szam += 1
    else:
        print("\nProgram vége!")


def f001_while_loop():
    # kiírja 10 és 20 között az egész számokat.
    # hátultesztelős, határozatlan lépésszámú
    szam = 10
    while True:
        print(szam)
        szam += 1
        if szam > 20:
            break


def f002_for():
    # kiírja 10 és 30 között a páros számokat.
    # elöltesztelős, határozott lépésszámú
    for i in range(10, 31, 2):
        print(i)


def f002_while():
    # kiírja 10 és 30 között a páros számokat.
    # elöltesztelős, határozatlan lépésszámú
    szam = 10
    while szam < 31:
        print(szam)
        szam += 2


def f002_while_loop():
    # kiírja 10 és 30 között a páros számokat.
    # hátultesztelős, határozatlan lépésszámú
    szam = 10
    while True:
        print(szam)
        szam += 2
        if szam > 30:
            break


def f003():
    # kiírja 100-tól 50-ig az öttel osztható számokat
    for i in range(100, 49, -5):
        print(i)


def f004():
    # bekér két számot és kiírja kettő közötti páros számokat
    szam1 = int(input("Kérek egy számot: "))
    szam2 = int(input("Kérek egy másik számot: "))
    kisebb = szam1 if szam1 < szam2 else szam2
    nagyobb = szam2 if szam2 > szam1 else szam1
    elsoparos = kisebb if kisebb % 2 == 0 else kisebb + 1
    for i in range(elsoparos, nagyobb + 1, 2):
        print(i)


def f005():
    # Nem negatív egész számról határozza meg a program, hogy hány jegyű!
    szam = int(input("Kérek egy nem negatív egész számot: "))
    helyiertekek_szama = 1
    seged = szam
    while seged > 10:
        helyiertekek_szama += 1
        seged = seged // 10
    print(f"{szam:,} szám {helyiertekek_szama} helyértéket tartalmaz")

#def f008():
    # Egy bekért számot kiír nullától növekvő, mellette lévő oszlopban nulláig csökkenő sorrendben

def f012():
    # százszor dob hatoldalú dobó kockával, és megmondja, hogy párosat vagy páratlant dobott többször.
    paros = 0
    paratlan = 0

    for dobasSzama in range(1, 101):
        veletlen = random.randint(1, 6)
        if veletlen % 2 == 1:
            paratlan += 1
        else:
            paros += 1

    if paros > paratlan:
        print(f"Páros volt több, {paros} darab.")
    elif paros < paratlan:
        print(f"Páratlan volt több, {paratlan} darab.")
    else:
        print(
            "Sosem gondoltam volna, de ilyen is van: \
            egyenlő a párosok és a páratlanok száma."
        )


def f098():
    szám = 999  # mindegy, csak páratlan legyen, hogy az első alkalommal belépjünk a ciklusba
    kísérlet = 0

    while szám % 2 != 0:
        kísérlet += 1
        szám = random.randint(1, 100)
        print(f"A(z) {kísérlet} dobás eredménye: ", szám, ".", sep="")

    print("A(z) ", kísérlet, ". dobás járt eredménnyel.", sep="")


# f001_for()
# f001_while()
# f001_while_loop()
# f002_for()
# f002_while()
# f002_while_loop()
# f003()
# f004()
f005()
print("\nProgram vége!")
