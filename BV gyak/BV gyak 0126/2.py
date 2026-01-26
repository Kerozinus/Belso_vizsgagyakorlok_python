szamok = [17, 5, 23, 281, 34, 51, 60, 39, 70]
megoldasok = []
for szam in szamok:
    if szam % 3 == 0:
        megoldasok.append(szam)
print(megoldasok[0],megoldasok[len(megoldasok)-1])
megoldasok = []
for szam in range(len(szamok)-1):
    if szamok[szam] > 50:
        print(szam+1)
        break
for szam in range(len(szamok)-1):
    if szamok[szam] > 20 and szamok[szam] < 40:
        print(szamok[szam])
        break
for szam in range(len(szamok)-1):
    if szamok[szam] == 281:
        print(szam+1)
        break