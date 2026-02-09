szam = int(input("Adj meg egy számot: "))
if szam % 2 == 0:
    print("A megadott számod páros.")
    print("A számod szorozva 14-el: ",szam*14)
elif szam % 2 == 1:
    print("A megadott számod páratlan.")
    print("A számod szorozva 14-el: ",szam*14)
else:
    print("A számod 0")