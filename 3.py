szamok = []
nr = 40
for i in range(40):
    bevitel = int(input(f"Adj meg még {nr} számot: "))
    nr -= 1
    szamok.append(bevitel)
eredmeny = szamok[0]
for osszeg in range(1,40):
    eredmeny = eredmeny + szamok[osszeg]
print(f"A számok összege : {eredmeny}")
eredmeny = szamok[0]
for kulonbseg in range(1,40):
    eredmeny = eredmeny - szamok[kulonbseg]
print(f"A számok különbsége (Az elsőből kivonva) : {eredmeny}")
eredmeny = szamok[0]
for szorzat in range(1,40):
    eredmeny = eredmeny * szamok[szorzat]
print(f"A számok szorzata: {eredmeny}")
eredmeny = szamok[0]
for hanyados in range(1,40):
    eredmeny = eredmeny - szamok[kulonbseg]
print(f"A számok hányadosa: {eredmeny}")