import math
import random

"""
Írj eljárást, mely a paraméterében kap két egész számot.
Ezen két egész szám közötti páros számok összegét számolja ki az eljárás.
"""

def feladat1(a:int, b:int):
    i:int = a
    osszeg=0
    while i < b:
        if i % 2 == 0:
            print(i)
            osszeg += i
        i+=1
    print(f"A páros számok összege: {osszeg}")
    return osszeg

def feladat1_2(a:int, b:int):
    osszeg=0
    for i in range(a, b, 1):
        if i % 2 == 0:
            print(i)
            osszeg += i
    print(f"A páros számok összege: {osszeg}")
    return osszeg


"""
írj függvényt, amely generál 10db véletlen számot: -10 és 10 között.
Számold meg hány negatív szám van közötte.
A visszatérési érték negatív számok száma.
"""


def negativ():
    i:int = 0
    while i <= 20:
        szam:int = math.floor(random.random()*21-10)
        print(szam)
        if szam < 0:
            db += 1
        i+=1
    return db

def negativ2():
    # i:int = 0
    db:int = 0
    for i in range(0, 20, 1):
        szam:int = math.floor(random.random()*21-10)
        print(szam)
        if szam < 0:
            db += 1
    return db

"""
Írj függvényt amely generál 10 véletlen számot 12 és 33 között és visszatér ezek összegével
"""

def veletlen_szam():
    vel_osszeg: int = 0
    for i in range(0, 10, 1):
        szam:int = math.floor(random.random()*(34-12)+12)
        vel_osszeg += szam
    return vel_osszeg

"""
Írj függvényt, amely generál 8 db véletlen számot, [20,50) intervallumban, és visszatér ezek közül a legnagyobb.
"""
def feladat3():
    max: int= 0
    for i in range(0, 8, 1):
        szam:int = math.floor(random.random()*(50-20)+20)
        if szam>max:
            max=szam
    return max


"""
Kérjünk be 3 db egész számot.
Mekkora a számok átlaga?
"""

def atlag():
    osszeg: int = 0
    for i in range(0, 3, 1):
        szam: int = int(input(f"Kérem az {i+1}, egész számot!"))
        osszeg += szam
    return osszeg/3

"""
Kérünk be a egész számokat a felhasználótól, amíg 0-t nem ad.
Írjuk ki a számok átlagát.
"""
def szamok():
    i: int = 0
    gyujto = 0
    szamlalo = 1
    szam:int = int(input("Adj meg egy számot!:" ))
    while szam!=0:
        gyujto += szam
        szamlalo += 1
        i += 1
        szam: int = int(input("Adj meg egy számot!:"))
    return gyujto/(szamlalo-1) # az utolsó megadott érték 0. Ahhoz, hogy ezt ne számolja belel kivonunk egyet


