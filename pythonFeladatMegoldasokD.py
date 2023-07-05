"""
Iterációk
"""
import random, os

os.system("cls")


def f097():
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
