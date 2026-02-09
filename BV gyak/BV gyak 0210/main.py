from datetime import datetime
adatok = []
sorokszama = 0
with open("D:/PROGI/Belso_vizsgagyakorlok_python/BV gyak/BV gyak 0210/tanulok.txt" , "r" ,encoding="utf-8") as f:
    for sor in f:
        adatok.append(sor.rstrip("\n").split(";"))
        sorokszama += 1
eredmeny = float(adatok[0][2])
for i in range(1,sorokszama):
    eredmeny = eredmeny + float(adatok[i][2])
eredmeny = eredmeny / sorokszama
with open ("D:/PROGI/Belso_vizsgagyakorlok_python/BV gyak/BV gyak 0210/eredmeny.txt","w",encoding="utf-8") as w:
    w.write(f"Fájl frissítve: {datetime.now()} \n")
    w.write("Tanulók száma: %i\n" % sorokszama)
    w.write("Az osztály átlaga: %.1f\n\n" % eredmeny)
    w.write("Jó tanulók: \n")
    for jo in range(sorokszama):
        if float(adatok[jo][2]) > 4.0:
            w.write(f"{adatok[jo][0]} {adatok[jo][2]}\n")