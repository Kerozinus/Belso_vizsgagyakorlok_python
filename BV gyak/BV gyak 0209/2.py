szamok = [8, 85, 522, 71, 4, 125, 23, 17, 14]
eredmeny = []
van = False
for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        eredmeny.append(szamok[i])
print(f"Az első a(z) {eredmeny[0]} és az utolsó {eredmeny[len(eredmeny)-1]} páros szám a listában")
eredmeny = []
for o in range(len(szamok)):
    if szamok[o] % 10 == 0:
        print(f"Az első 10-el osztható szám a {o+1}. helyen van")
        van = True
        break
    if o == 8 and van == False:
        print("A listában nincs 10-el osztható szám")
for x in range(len(szamok)):
    if szamok[x] > 0 and szamok[x] < 6:
        print(f"Az első 0 és 6 közé eső szám a : {szamok[x]}")
        break
for a in range(len(szamok)):
    if szamok[x] == 14:
        print(f"A {x+1}. helyen van a 14")