"""
sztringek
"""
import os

os.system("cls")


def f001():
    # Bekér egy szöveget és betűnként új sorba kiírja.
    szoveg = input("Kérek egy szöveget: ")
    for i in range(len(szoveg)):
        print(szoveg[i])


def f002():
    # Bekér egy szöveget és fordított irányban kiírja.
    szoveg = input("Kérek egy szöveget: ")
    forditott = ""
    for i in range(len(szoveg)):
        forditott += szoveg[len(szoveg) - i - 1]
    print(forditott)


def f003():
    # Bekér egy szöveget és megszámolja, melyik betűből hány darab van benne.
    szoveg = input("Kérek egy szöveget: ")
    unique_characters = set(szoveg)
    for letter in unique_characters:
        print(f"{letter} => {sum(c == letter for c in szoveg)}")
    print()


# f001()
# f002()
f003()
