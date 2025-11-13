"""
A program személyek nevét és annak éves átlagát (jegy) kéri be. 

Eldönti és kiírja, hogy a személy az átlag alapján hányas osztályzatot érdemel, 
amit szövegesen meg is jelenít. 

Az átlagból következő jegy 
1-2 között elégtelen: 
2,1-2,61 között: elégséges; 
2,62-3,61 között: közepes; 
3,62-4,61 között: 
jó.4,62-5 között: jeles.

"""

# 1. személyek és jegyek bekérése
# 2. Folyamatos bekérés -> amíg nem üres a név mező
nev = input("Kérek egy nevet: ")

while nev != "":

    atlag = float(input("Kérem az átlagot: "))
    nev = input("Kérek egy nevet: ")