#Napraviti generator funkcije za ispis svih parnih
#i svih neparnih brojeva manjih od prosljeđenog
#parametra.
def parni_neparni(broj):
    for i in range(broj):
        if i%2==0:
            yield i,"paran"
        else:
            yield i,"neparan"
generator=parni_neparni(10)
for broj,status in generator:
    print("Broj: " +str(broj) + " je " + str(status))

