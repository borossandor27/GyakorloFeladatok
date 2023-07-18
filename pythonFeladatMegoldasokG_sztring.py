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


def f004():
    # Bekér egy szöveget és kiírja ’e’ betűk nélkül.
    szoveg = input("Kérek egy szöveget: ")
    enelkul = ""
    for letter in szoveg.lower():
        if letter != "e":
            enelkul += letter
    print(enelkul)

def f005():
    # Bekér egy szöveget és kiírja, hogy van-e benne névelő (’a’ vagy ’az’) 
    szoveg = input("Kérek egy szöveget: ")
    if szoveg.lower().rfind(' a ') >= 0 or szoveg.lower().rfind(' az ')>=0 or szoveg.lower().startswith('a ') or szoveg.lower().startswith('az '):
        print(f"\n'{szoveg}' szöveg tartalmaz névelőt.\n")
    else:
        print(f"\n'{szoveg}' szöveg NEM tartalmaz névelőt.\n")
def f006():
    # Bekér egy szöveget és csak a benne lévő magánhangzókat írja ki. (aáeéiíoóöőuúüű)  
    szoveg = input("Kérek egy szöveget: ")
    maganhangzokNelkul=''
    for letter in szoveg.lower():
        if "aáeéiíoóöőuúüű".rfind(letter) < 0: 
            maganhangzokNelkul += letter
    print(f"\n'{szoveg}' szöveg magánhangzók nélkül '{maganhangzokNelkul}'\n")

# f001()
# f002()
# f003()
#f004()
#f005()
f006()
