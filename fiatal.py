from operator import le
import allat
kutyak = []
for i in range(3):
    nev = input("Adja meg egy tanuló nevét! ")
    fajta = int(input("Adja meg a magyar jegyét! "))
    kor = int(input("Adja meg a matematika jegyét! "))
    egykutya= allat.Kutyam(nev, fajta, kor, )
    kutyak.append(egykutya)

legfiatalabb_kutya = kutyak

for egykutya in kutyak:
    print(egykutya.nev,'egy', egykutya.fajta,'és',egykutya.kor,'éves')
    if egykutya.kor < legfiatalabb_kutya.kor:
        legfiatalabb_kutya = egykutya

#for t in tanulok:
   # print(f"{t.nev} átlaga:{t.atlag}")
    #print("{} átlaga:{}".format(t.nev, t.atlag))
#legjobb = tanulok[0]
#for t in tanulok[1:]:
    #if t.atlag > legjobb.atlag:
     #   legjobb = t
#with open(file="legjobb.txt", mode="w", encoding="utf-8") as f:
 #   f.write(legjobb.nev)