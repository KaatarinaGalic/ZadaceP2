import re

regex_Email = '^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
reg_eduid = '^[a-z]{1}[a-zA-Z]+\d*@sum\.ba$'

unos_Email=input("| Unesite Vaš Email: ")


if re.match(regex_Email, unos_Email):
    print("Unesena E-mail adresa je ispravna.")
else:
    print(" Unesena E-mail adresa nije ispravna.")

print("\n")  
unos_EduId=input("| Unesite Vaš EduId: ")

if re.match(reg_eduid, unos_EduId):
    print("EduId je ispravan.")
else:
    print("EduId nije ispravan.")
