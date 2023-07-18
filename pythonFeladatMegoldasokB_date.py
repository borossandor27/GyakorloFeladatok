"""
Dátummal és idővel kapcsolatos feladatok 

"""
from os import system
from datetime import datetime, timedelta, date
import locale

locale.setlocale(locale.LC_ALL, "hu_HU.UTF-8")

system("cls")


def f001():
    # Bekér egy dátumot és kiírja, a hét melyik napjára esik.
    datumString = input("Adjon meg egy dátumot (éééé-hh-dd) formátumban: ")
    datum = datetime.strptime(datumString, "%Y-%m-%d").date()
    print(f"\n{datum} {hetNapja(datum)}\n")


def f002():
    # Bekér egy dátumot és magyarul írja ki, hogy a hét melyik napjára esik.
    datumString = input("Adjon meg egy dátumot (éééé-hh-dd) formátumban: ")
    datum = datetime.strptime(datumString, "%Y-%m-%d").date()

    print(f"\n{datum} {hetNapja(datum)}\n ")


def f003():
    # Bekér két dátumot és kiírja a kettő között eltelt napok számát.
    datumKezd = datetime.strptime(
        input("Adja meg a kezdő dátumot (éééé-hh-dd) formátumban: "), "%Y-%m-%d"
    ).date()
    datumVeg = datetime.strptime(
        input("Adja meg a befejezés dátumot (éééé-hh-dd) formátumban: "), "%Y-%m-%d"
    ).date()
    print(
        f"\n{datumKezd} és {datumVeg} között {str((datumVeg-datumKezd).days)} nap telt el.\n"
    )


def f004():
    # Bekér egy dátumot és a négy héttel későbbi dátumot írja ki.
    datum = datetime.strptime(
        input("Adja meg a kezdő dátumot (éééé-hh-dd) formátumban: "), "%Y-%m-%d"
    ).date()
    print(f"\n{datum}  4 héttel későbbi dátum {datum+timedelta(days=14)}\n")


def f005():
    # Az aktuális hónap-nap az előző évben milyen napra esett?
    datum = datetime.strptime(
        input("Adja meg a dátumot (éééé-hh-dd) formátumban: "), "%Y-%m-%d"
    ).date()
    ev = datum.year - 1
    honap = datum.month
    nap = datum.day
    elozoEviDatum = date(ev, honap, nap)
    print(f"\n{datum}  az előző évben {hetNapja(elozoEviDatum)} volt\n")


def f006():
    # Ön hány napos?
    szuletett = datetime.strptime(
        input("Adja meg a születési dátumot (éééé-hh-dd) formátumban: "), "%Y-%m-%d"
    ).date()
    print(
        f"\n {szuletett} dátum óta {str((date.today()-szuletett).days)} nap telt elt .\n"
    )


def hetNapja(datumErtek):
    match datumErtek.weekday():
        case 0:
            return "hétfő"
        case 1:
            return "kedd"
        case 2:
            return "szerda"
        case 3:
            return "csütörtök"
        case 4:
            return "péntek"
        case 5:
            return "szombat"
        case 6:
            return "vasárnap"
        case _:
            return "ismeretlen"


# f001()
# f002()
# f003()
# f004()
# f005()
f006()
