lista = []
for i in range(2):
    bevitel = int(input("Add meg az intervallum felső és alsó értékét: "))
    lista.append(bevitel)
also = min(lista[0],lista[1])
felso = max(lista[0],lista[1])
vegeredmeny = 0
for x in range(also,felso):
    if x % 2 == 0:
        vegeredmeny = vegeredmeny + x
print(vegeredmeny)

