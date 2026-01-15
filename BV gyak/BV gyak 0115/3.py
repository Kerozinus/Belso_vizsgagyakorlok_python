from random import randint
szamok = []
szam_nr = 0
for i in range(10):
    szamok.append(randint(20,80))
print("A generált számok:",",".join(str(szam)for szam in szamok))
keresettszam = int(input("Melyik számot keressem meg a listában: "))
print("A megadott szám %i-szor szerepel a listában. " % szamok.count(keresettszam))
szamok[0] = keresettszam
print("Az új lista:",",".join(str(szam)for szam in szamok))
