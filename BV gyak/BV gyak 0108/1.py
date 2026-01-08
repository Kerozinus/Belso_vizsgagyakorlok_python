bevitel = int(input("Add meg az alkatrész árát egész számmal: "))
noveles = float(input("Hány %-al szeretnéd növelni az árat? "))
eredmeny = (noveles/100+1)*bevitel
print("%i" % eredmeny)