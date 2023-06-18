with open('REZ.csv', 'r') as f:
    linije = f.readlines()
    data = []
    for linija in linije:
        element = linija.strip().split(';')
        ime, prezime, bodovi, naziv = element
        print (tuple(element))
        data.append((ime, prezime, int(bodovi), naziv))

    for ime, prezime, bodovi, naziv in data:
        if int(bodovi)>49:
            print(ime, prezime, " je položio ispit sa" ,bodovi, "bodova.")

data.sort(key=lambda x: x[1])
print("Sortirano po prezimenima:",data)



bodovi_rang ={
    "Nedovoljan":[],
    "Dovoljan":[],
    "Dobar":[],
    "Vrlo dobar":[],
    "Odličan":[]
    }
for ime, prezime, bodovi, naziv in data:
    if bodovi < 50:
        bodovi_rang["Nedovoljan"].append(prezime)
    elif bodovi < 66:
        bodovi_rang["Dovoljan"].append(prezime)
    elif bodovi < 81:
        bodovi_rang["Dobar"].append(prezime)
    elif bodovi < 91:
        bodovi_rang["Vrlo dobar"].append(prezime)
    else:
        bodovi_rang["Odličan"].append(prezime)

print(bodovi_rang)

for bodovi, studenti in bodovi_rang.items():
    print(f"{bodovi}: {len(studenti)}")
    print('\n'.join(studenti))
