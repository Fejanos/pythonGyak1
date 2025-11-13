"""
A program kérjen be a felhasználótól egy számot, 
majd írja ki, hogy az osztható-e maradék nélkül 9-cel!
"""

# 1. bekérés
szam = int(input("Kérek egy számot: "))

# 2. eldöntés
if szam % 9 == 0:
    print(f"A {szam} osztható 9-cel")
else:
    print(f"A {szam} nem osztható 9-cel")