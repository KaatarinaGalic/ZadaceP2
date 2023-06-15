'''
imena=[]
prezimena=[]
def unosUcenika(ime,prezime):
    imena.append(ime)
    prezimena.append(prezime)
while 1:
    a=input("Unesite ime:")
    b=input("Unesite prezime:")
    if a=='x' or a=='X' or b=='x' or b=='X':
        break
    unosUcenika(a,b)
sifra_ucenika=len(imena)
for i in range(sifra_ucenika):
    print(imena[i], prezimena[i], i)
import random
x=random.randrange(sifra_ucenika)
print("otvoren je", imena[x], prezimena[x])
'''    
artikli=[]
cijene=[]
def dodajArtikl(naziv,cijena):
    artikli.append(naziv)
    cijene.append(cijena)

for i in range(5):
    naziv=input("Unesite naziv:")
    cijena=float(input("Unesite cijenu:"))
    dodajArtikl(naziv,cijena)

print("------Cjenik-------")
for i in range(5):
    print(i,artikli[i],cijene[i])
racun=[]
while 1:
    sifra=input("Unesite sifru artikla:")
    if (sifra.lower()=='x'):
        break
    sifra=int(sifra)
    print("odabrani artikal:", artikli[sifra],"po ijeni:", cijene[sifra])
    kolicina=float(input("Unesite kolicinu:"))
    total=cijene[sifra]*kolicina
    racun.append(total)
print("----------------")
print("---------Vaš račun----------")
print("Total:", sum(racun))
    
