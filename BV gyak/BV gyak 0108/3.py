import random
lista = []
nr = 0
for i in range(15):
    lista.append(random.randint(20,80))
bevitel = int(input("Adj meg egy számot 20 és 80 között: "))
for elem in lista:
    if elem == bevitel:
        nr+=1
print(nr)
lista[0] = bevitel
print(lista)