szam = int(input("Adj meg egy egész számot: "))
if szam > 0:
    print("A számod pozitív")
    print("A számod 3szorosa: ",szam*3)
elif szam < 0:
    print("A számod negatív")
    print("A számod 3szorosa: ",szam*3)
else:
    print("A számod nulla")
    print("Mit szeretnél még csinálni? 0*3=0 agytekervény")