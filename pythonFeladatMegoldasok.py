"""
Az INFORMATIKA ÉS TÁVKÖZLÉS ágazathoz tartozó 
- 5 0613 12 03 SZOFTVERFEJLESZTŐ ÉS –TESZTELŐ SZAKMA
- 5 0612 12 02INFORMATIKAI RENDSZER- ÉS ALKALMAZÁSÜZEMELTETŐ TECHNIKUS SZAKMA

Ágazati alapvizsga követelményeire felkészítő egyszerű feladatok
"""
import os, math


def f01():
    # Kérjünk be a felhasználótól két egész számot, majd adjuk meg az összegüket, a hányadosukat.
    os.system("cls")
    egeszSzam01 = int(input("Kérem adjon meg egy egész számot: "))
    egeszSzam02 = int(input("Kérem adjon meg egy egész számot: "))
    print(f"\nA {egeszSzam01} és {egeszSzam02} összege: {egeszSzam01 + egeszSzam02}")
    print(
        f"\nA {egeszSzam01} és {egeszSzam02} hányadosa: {(egeszSzam01 / egeszSzam02):.2f}"
    )


def f02():
    # Kérjünk be a felhasználótól egy pozitív egész számot, majd adjuk meg a kettővel és a hárommal vett osztási maradékát.
    os.system("cls")
    egeszSzam01 = int(input("Kérem adjon meg egy pozitív egész számot: "))
    print(f"\nA {egeszSzam01} kettővel osztás maradéka: {egeszSzam01 % 2}")
    print(f"\nA {egeszSzam01} hárommal osztás maradéka: {egeszSzam01 % 3}")


def f03():
    # Kérjünk be a felhasználótól egy páros számot, majd adjuk meg a felét.
    os.system("cls")
    parosSzam01 = int(input("Kérem adjon meg egy páros számot: "))
    print(f"\nA {parosSzam01} fele: {parosSzam01 / 2}")


def f03b():
    # Kérjünk be a felhasználótól egy páros számot, majd adjuk meg a felét.
    # Ha már ismernéd a ciklus utasítást, akkor ki is lehetne kényszeríteni a páros értéket
    os.system("cls")
    parosSzam01 = 0
    while True:
        parosSzam01 = int(input("Kérem adjon meg egy páros számot: "))
        if parosSzam01 % 2 == 0:
            break
    print(f"\nA {parosSzam01} fele: {parosSzam01 / 2}")


def f04():
    # Kérjünk be a felhasználótól egy valós számot, majd adjuk meg a harmadát.
    os.system("cls")
    valosSzam = float(input("Kérem adjon meg egy valós értéket: "))
    print(f"A {valosSzam} szám haramada: {(valosSzam/3):.3f}")


def f05():
    # Kérjük be a felhasználótól egy kör alakú medence átmérőjét és mélységét, majd adjuk meg, hogy hány köbméter víz fér bele.
    os.system("cls")
    atmero = float(input("Kérem adja meg a medence átmérőjét méterben: "))
    magassag = float(input("Kérem adja meg a medence magasságát méterben: "))
    terfogat = math.pi * math.pow(atmero / 2, 2) * magassag
    print(
        f"A {atmero} m átmérőjű és {magassag} m magasságú medence térfogta: {(terfogat):.3f} m"
        + "\u00b3"
    )


def f06():
    # Oldja meg az 'ax + b = 0'  alakú elsőfokú egyenletet! 
    os.system("cls")
    a = float(input("Kérem adja meg az 'ax + b = 0' egyenlet 'a' értékét: "))
    b = float(input("Kérem adja meg az 'ax + b = 0' egyenlet  'b' értékét: "))
    print(f"\nx értéke: {(-b/a):.4f}")


def main():
    # f01()
    # f02()
    # f03()
    # f03b()
    # f04()
    # f05()
    f06()


main()
