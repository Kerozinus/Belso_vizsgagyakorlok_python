szam = int(input("Adj meg egy egész számot: "))
if szam > 0:
    print("A számod pozitív")
    print("A számod 5szorosa: ",szam*5)
elif szam < 0:
    print("A számod negatív")
    print("A számod 5szorosa: ",szam*5)
else:
    print("A számod nulla")
    print("Mit szeretnél még csinálni? 0*5=0 agytekervény")