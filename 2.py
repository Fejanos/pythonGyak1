"""
A program személyek nevét és annak éves átlagát (jegy) kéri be. 

Függvény:
Eldönti és kiírja, hogy a személy az átlag alapján hányas osztályzatot érdemel, 
amit szövegesen meg is jelenít. 

Az átlagból következő jegy 
1-2 között elégtelen: 
2,1-2,61 között: elégséges; 
2,62-3,61 között: közepes; 
3,62-4,61 között: jó.
4,62-5 között: jeles.

"""

# Függvény mindig a tetején!
# def megnevezés(paraméter lista):
def osztalyzat(param_atlag):
    if param_atlag <= 2:
        print("elégtelen")
    elif param_atlag <= 2.61 and param_atlag >= 2.1:
        print("elégséges")
    elif param_atlag <= 3.61 and param_atlag >= 2.62:
        print("közepes")
    elif param_atlag <= 4.61 and param_atlag >= 3.62:
        print("jó")
    else:
        print("jeles")

# 1. személyek és jegyek bekérése
# 2. Folyamatos bekérés -> amíg nem üres a név mező
nev = input("Kérek egy nevet: ")

while nev != "":

    atlag = float(input("Kérem az átlagot: "))
    nev = input("Kérek egy nevet: ")