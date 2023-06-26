"""
Az INFORMATIKA ÉS TÁVKÖZLÉS ágazathoz tartozó 
- 5 0613 12 03 SZOFTVERFEJLESZTŐ ÉS –TESZTELŐ SZAKMA
- 5 0612 12 02INFORMATIKAI RENDSZER- ÉS ALKALMAZÁSÜZEMELTETŐ TECHNIKUS SZAKMA

Ágazati alapvizsga követelményeire felkészítő egyszerű feladatok
"""
import os


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


def main():
    # f01()
    # f02()
    # f03()
    f03b()


main()
