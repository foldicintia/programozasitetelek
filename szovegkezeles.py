# I. Kérjünk be egy szöveget és végezzük el rajta a következő műveleteket, 
# majd minden végeredmény jelenítsünk meg a képernyőn még akkor is, ha ezt a feladat külön nem írja! (konzolos feladat)

# Írj metodust, mely paraméterében kap egy szöveget: 
# 1.Számoljuk meg hány szóköz van a szövegben! 

def szokoz(szoveg:str):
    db = 0
    i = 0
    while i < len(szoveg):
        if szoveg[i]== " ":
            db += 1
        i += 1
    return db

# 2. Írjuk ki a szöveget a képernyőre szóközök nélkül. A továbbiakban ezzel a szöveggel dolgozzunk!

def szokoz_nelkul(szoveg:str):
    i = 0
    uj_szoveg: str = " "
    while i < len(szoveg):
        if not (szoveg[i]== " "):
            uj_szoveg+=szoveg[i]
        i+=1
    return uj_szoveg

# 3.Alakítsuk a szöveget kisbetűssé! A továbbiakkal ezzel a szöveggel dolgozzunk!

def kisbetus(uj_szoveg:str):
    uj_szoveg=uj_szoveg.lower()
    uj_szoveg=uj_szoveg.replace("é","e")
    uj_szoveg=uj_szoveg.replace("í","i")
    uj_szoveg=uj_szoveg.replace("ö","o")
    uj_szoveg=uj_szoveg.replace("ő","ö")
    uj_szoveg=uj_szoveg.replace("ó","o")
    uj_szoveg=uj_szoveg.replace("á","a")
    uj_szoveg=uj_szoveg.replace("ü","u")
    uj_szoveg=uj_szoveg.replace("ú","u")
    uj_szoveg=uj_szoveg.replace("ű","u")

    i = len(uj_szoveg) -1
    while 1 >= 0:
        print(szoveg[i], end= " ")
        i -= 1

def hazi1():
    # Számold meg, hogy hány darab 7-tel osztható szám van 1-1000 között!
    print("1.feladat")
    szamlalo = 0
    for i in range(1, 1001, 1):
        if i % 7 == 0:
            szamlalo += 1
    print(f"0 és 1000 között {szamlalo} darab 7-tel osztható szám van.")


def hazi2():
    # Számold meg, hogy hány darab 12-vel osztható szám van 2000-20000 között!
    print("2.feladat")
    szamlalo = 0
    for i in range(2000, 20001, 1):
        if i % 3 == 0 and i % 4 == 0:
            szamlalo += 1
    print(f"2000 és 20000 között {szamlalo} darab 12-vel osztható szám van.")

def hazi3():
    # Írd ki az első 20 3-mal osztható szám négyzetének összegét!
    print("3.feladat")
    i = 1
    gyujto = 0
    negyzet = 0
    while i <= 20:
        if i % 3 == 0:
            negyzet = i ** 2
            gyujto += negyzet
        i += 1
    print(f"Az első 20 3-mal osztható szám összege: {gyujto}")


def hazi4(szam:int):
    #4 Keresd meg egy szám egész osztóit!
    print("4.feladat")
    