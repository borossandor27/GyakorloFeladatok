"""
Tömbök, listák
"""
import os, random

os.system("cls")


def f001():
    # Feltölt egy 10 elemű tömböt 1 és 100 közötti egészekkel és kiírja az átlagot meghaladó értékeket.
    tomb = []
    for i in range(10):
        tomb.append(random.randint(1, 100))
    print(tomb)
    atlag = 0.0
    for ertek in tomb:
        atlag += ertek
    atlag /= 10.0
    print(f"\n\tSzámtani átlaguk: {atlag:.2f} ")
    print(f"\n\tÁtlag feletti értékek:")
    atlagFelettiek = []
    for ertek in tomb:
        if ertek > atlag:
            atlagFelettiek.append(ertek)
    print("\t",atlagFelettiek)


f001()
