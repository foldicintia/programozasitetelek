import feladatok

feladatok.feladat1(20, 52)

"""
írj függvényt, amely generál 10db véletlen számot: -10 és 10 között.
Számold meg hány negatív szám van közötte.
A visszatérési érték negatív számok száma.
"""

negativ_db: int = feladatok.negativ()
print(f"A negatív számok száma: {negativ_db}")


"""
Írj függvényt, amely generál 8 db véletlen számot, [20,50) intervallumban, és visszatér ezek közül a legnagyobb.
"""

vel_osszeg: int = feladatok.veletlen_szam()
print(f"A véletlen számok összege: {vel_osszeg}")


"""
Kérjünk be 3 db egész számot.
Mekkora a számok átlaga?
"""
feladatok.feladat3()
feladatok.atlag()

feladatok.szamok()

