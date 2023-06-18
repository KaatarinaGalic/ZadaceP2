import re

ime_prezime = "Katarina Galić"
regex_izraz = r"^" + ime_prezime[0] + r".*[0-5].*\s" + ime_prezime[-1] + r"$"

unos = input("Unesite string: ")
if re.match(regex_izraz, unos):
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")
