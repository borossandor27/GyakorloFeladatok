"""
Szelekciók
"""
import os
import math

os.system("cls")


def f001():
    # Kérjünk be a felhasználótól két egész számot, majd írassuk ki a nagyobbat.
    szam1 = int(input("Kérek egy egész számot: "))
    szam2 = int(input("Kérek egy másik egész számot: "))
    if szam1 > szam2:
        print(f"\n{szam1} a nagyobb\n")
    elif szam1 < szam2:
        print(f"\n{szam2} a nagyobbat\n")
    else:
        print(f"\n{szam1} és {szam2} értéke megegyezik\n")


def f002():
    # Kérjünk be a felhasználótól két egész számot, majd adjuk meg a két szám különbségét. A nagyobból vonjuk ki a kisebbiket.
    szam1 = int(input("Kérek egy egész számot: "))
    szam2 = int(input("Kérek egy másik egész számot: "))
    if szam1 > szam2:
        print(f"\n{szam1} - {szam2} = {szam1-szam2}\n")
    elif szam2 > szam1:
        print(f"\n{szam2} - {szam1} = {szam2-szam1}\n")
    else:
        print(f"\n{szam1} és {szam2} egyenlő\n")


def f003():
    # Kérjünk be egy egész számot a felhasználótól. Vizsgáljuk meg, hogy osztható-e 10-el.
    # Ha osztható, akkor az alábbi mondatot írjuk ki a képernyőre: “A szám osztható 10-zel.”
    # Ha nem teljesül az oszthatóság írjuk ki a képernyőre a szám 10-zel vett osztásának maradékát.
    szam = int(input("Kérek egy egész számot: "))
    if szam % 10 == 0:
        print("\nA szám osztható 10-zel.\n")
    else:
        print(f"\nA szám 10-zel vett osztásának maradéka {szam%10}.\n")


def f004():
    # Kérjünk be két egész számot a felhasználótól, amely egy közönséges tört számlálója és nevezője.
    # Írjuk ki a valós értékét. Írjunk ki hiba üzentet, ha a tört nevezője nulla lenne.
    szamlalo = int(input("Kérem a tört számlálóját: "))
    nevezo = int(input("Kérem a tört nevezőjét: "))
    if nevezo == 0:
        print(f"\nnullával nem lehet osztani!\n")
    else:
        print(f"\n{szamlalo} / {nevezo} értéke {(szamlalo/nevezo):.4f}\n")


def f005():
    # Készíts programot, amely bekér egy háromjegyű pozitív egész számot, és eldönti róla, hogy Armstrong szám e.
    # Az Armstrong számokra igaz, hogy a számjegyei köbének összege megegyezik az eredeti számmal.
    szam = int(input("Kérek egy háromjegyű egész számot: "))
    if szam < 100 or szam > 999:
        print("\nNem háromjegyű számot adott meg\n")
    else:
        szazas = szam // 100
        tizes = (szam - szazas * 100) // 10
        egyes = szam % 10
        if szam == math.pow(szazas, 3) + math.pow(tizes, 3) + math.pow(egyes, 3):
            print(f"\n{szam} Armstrong szám.\n")
        else:
            print(f"\n{szam} NEM Armstrong szám.\n")


def f006():
    # Írjunk programot, ami bekér a felhasználótól egy egész számot,
    # majd az alábbi mondatok közül kiírja azokat a képernyőre, amelyek igazak
    szam = int(input("Kérek egy egész számot: "))
    if szam == 4:
        print("A megadott szám a 4-es. ")
    if szam < 10:
        print("A megadott kisebb mint 10. ")
    if szam % 2 == 0:
        print("A megadott szám páros. ")
    if szam > 0 and szam < 10:
        print("A megadott a [0,10] intervallumba esik. ")
    if szam % 3 == 0 and szam % 5 == 0:
        print("A megadott szám osztható 3-mal és 5-tel is. ")
    if szam <= 10 or szam >= 20:
        print("A megadott szám nem a [10,20] intervallumba esik. ")


def f007():
    # Írjunk programot, ami bekér a felhasználótól két egész számot,
    # majd az alábbi mondatok közül kiírja azokat a képernyőre, amelyek igazak
    szam1 = int(input("Kérek egy egész számot: "))
    szam2 = int(input("Kérek egy másik egész számot: "))
    if szam1 == szam2:
        print("A két szám egyenlő. ")
    if szam1 % 2 == 1 and szam2 % 2 == 1:
        print("Mind a két szám páratlan. ")
    if szam1 % 3 == 0 or szam2 % 3 == 0:
        print("Legalább az egyik szám osztható hárommal. ")
    if szam1 < 0 and szam2 < 0:
        print("Mind a két szám negatív. ")
    if (szam1 < 0 and szam2 > 0) or (szam1 > 0 and szam2 < 0):
        print("Az egyik szám negatív, a másik szám pozitív. ")


def f032():
    # Húsvét vasárnap számítása
    T = int(input("\nKérem az évszámot: "))
    A = T % 19
    B = T % 4
    C = T % 7
    D = (19 * A + 24) % 30
    E = (2 * B + 4 * C + 6 * D + 5) % 7
    H = 22 + D + E
    if E == 6 and D == 29:
        H = 50
    elif E == 6 and D == 28 and A > 10:
        H = 49

    ev = T
    honap = "március"
    if H > 31:
        H -= 31
        honap = "április"
    nap = H

    print(f"\n{ev}. évben Húsvét vasárnap {honap} hó {nap}. napjára esik")


# f001()
# f002()
# f003()
# f004()
# f005()
# f006()
f007()
# f032()
