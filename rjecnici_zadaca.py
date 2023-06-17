#Koristeći listu imena iz prethodnog zadatka svakom studentu generirati
#nasumičnu ocjenu od 1 do 5.Prebrojati u rječnik koliko ima kojih ocjena.
#Izračunati postotak prolaznosti. (sve ocjene veće od 1)
lista=['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka', 'Antonio',
'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David', 'Ivan', 'Petar', 'Marija',
'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan',
'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']
import random
rjecnik={}
ocjene_studenata={}
for ime in lista:
    ocjena=random.randint(1,5)
    rjecnik[ime]=ocjena
    if ocjena in ocjene_studenata:
        ocjene_studenata[ocjena]+=1
    else:
        ocjene_studenata[ocjena]=1
print(ocjene_studenata)
brojac=0
brojac_2=0
for ocjena in rjecnik.values():
    if ocjena>1:
        brojac_2+=1
        brojac+=ocjena

print("Postotak prolaznosti iznosi:", (brojac/brojac_2))
    
