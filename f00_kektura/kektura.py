import os, codecs


class Szakasz:
    def __init__(self, sor, tengerszintFelettIndulaskor):
        items = sor.strip().split(";")
        self.kiindulopont = items[0]
        self.vegpont = items[1]
        self.hossza = float(items[2].replace(",", "."))
        self.emelkedes = int(items[3])
        self.lejtes = int(items[4])
        self.pecsetelohely = True if items[5] == "i" else False
        self.tengerszintFelettIndulaskor = tengerszintFelettIndulaskor
        self.tengerszintFelettVegpontnal = (
            tengerszintFelettIndulaskor + self.emelkedes - self.lejtes
        )

    def __str__(self):
        textOutput = [
            self.kiindulopont,
            self.vegpont,
            str(self.hossza),
            str(self.emelkedes),
            str(self.lejtes),
            'i' if self.pecsetelohely else 'n'
        ]
        return "\n" + ";".join(textOutput)


szakaszok = []
turaKiindulopontTengerszintfelettiMagassaga = None


def beolvas():
    global turaKiindulopontTengerszintfelettiMagassaga
    file = open("kektura.csv", encoding="UTF-8")
    turaKiindulopontTengerszintfelettiMagassaga = int(file.readline())
    kiindulopontTengerszintfelettiMagassaga = (
        turaKiindulopontTengerszintfelettiMagassaga
    )
    for sor in file:
        szakasz = Szakasz(sor, kiindulopontTengerszintfelettiMagassaga)
        szakaszok.append(szakasz)
        kiindulopontTengerszintfelettiMagassaga = szakasz.tengerszintFelettVegpontnal


def f03():
    print(f"\n3. feladat: Szakaszok száma: {len(szakaszok)} db")


def f04():
    hossz = 0
    for szakasz in szakaszok:
        hossz += szakasz.hossza
    print(f"\n4. feladat: A túra teljes hossza: {hossz:.3f} km")


def f05():
    print(f"\n5. feladat: A legrövidebb szakasz adatai:")
    legrovidebbSzakasz = szakaszok[0]
    legrovidebbHossz = legrovidebbSzakasz.hossza
    for szakasz in szakaszok:
        if szakasz.hossza < legrovidebbHossz:
            legrovidebbSzakasz = szakasz
            legrovidebbHossz = legrovidebbSzakasz.hossza
    print(f"\tKezdete: {legrovidebbSzakasz.kiindulopont}")
    print(f"\tVége: {legrovidebbSzakasz.vegpont}")
    print(f"\tTávolság: {legrovidebbSzakasz.hossza:,} km")


def HianyosNev(vegpont):
    return not "pecsetelohely" in vegpont


def f07():
    print(f"\n7. feladat: Hiányos állomásnevek:")
    for szakasz in szakaszok:
        if szakasz.pecsetelohely and HianyosNev(szakasz.vegpont):
            print(f"\t{szakasz.vegpont}")


def f08():
    print(f"\n8. feladat: A túra legmagasabban fekvő végpontja:")
    legmagasabbSzakasz = szakaszok[0]
    legmagasabbPont = legmagasabbSzakasz.tengerszintFelettVegpontnal
    for szakasz in szakaszok:
        if szakasz.tengerszintFelettVegpontnal > legmagasabbPont:
            legmagasabbSzakasz = szakasz
            legmagasabbPont = legmagasabbSzakasz.tengerszintFelettVegpontnal
    print(f"\tA végpont neve: {legmagasabbSzakasz.vegpont}")
    print(
        f"\tA végpont tengerszint feletti magassága: {legmagasabbSzakasz.tengerszintFelettVegpontnal} m"
    )


def f09():
    print(f"\n9. feladat: kektura2.csv szöveges állomány elkészítése")
    file = codecs.open("kektura2.csv", "w", "utf-8")
    file.write(str(turaKiindulopontTengerszintfelettiMagassaga))
    for szakasz in szakaszok:
        szakasz.vegpont += (
            " pecsetelohely"
            if ("pecsetelohely" not in szakasz.vegpont and szakasz.pecsetelohely)
            else ""
        )
        szakasz
        sor = szakasz.__str__()
        file.write(sor)
    file.close()


os.system("cls")
beolvas()
f03()
f04()
f05()
f07()
f08()
f09()
print("\nProgram vége!")
