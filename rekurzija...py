#Napisati rekurzivnu funkciju koja kao parametar prima string,
#a kao rezultat taj string ispisuje sa zada

def zadnji(r):
    if len(r)==0:
        return ""
    else:
         return r[-1]+zadnji(r[:-1])

unos=input("Unesite neku rijec:")
rez=zadnji(unos)
print(rez)
