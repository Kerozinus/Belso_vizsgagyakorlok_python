a=int(input("Írd be az első számot: "))
b=int(input("Írd be a második számot: "))
szamok = []
asd = None
oszthato_4 = 0
if a < b:
    for i in range(a,b+1):
        szamok.append(i)
        if i % 4 == 0:
            oszthato_4 = oszthato_4 + 1
print("Az alábbi számokat találtam: ",",".join(str(szam) for szam in szamok))
print("A két szám között %i db szám van, ami osztható 4-el." % oszthato_4)
