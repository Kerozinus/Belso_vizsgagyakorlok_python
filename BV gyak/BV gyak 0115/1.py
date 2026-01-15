type = input("Milyen mértékegységben adod meg: ")
nr = int(input("Írd be az átváltandó számot: "))
if type == "MB":
    print((nr/1.024)/1000,"GB")
if type == "GB":
    print((nr*1.024)*1000,"MB")