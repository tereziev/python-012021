"""
Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

Datum 	                    Cena
1. 7. 2021 - 10. 8. 2021 	250 Kč
11. 8. 2021 - 31. 8. 2021 	180 Kč

Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit.
Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené.
Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.

Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if.
Níže vidíš příklad porovnání dvou dat. Program vypíše text "První datum je dřívější než druhé datum.".

from datetime import datetime
prvni_udalost = datetime(2021, 7, 1)
druha_udalost = datetime(2021, 7, 3)
if prvni_datum < druhe_datum:
  print("Druhá událost se stala po první události")
"""
from datetime import datetime, timedelta

sezona1_start = datetime(2021, 7, 1)
sezona1_end = datetime(2021, 8, 10)
sezona2_start = datetime(2021, 8, 11)
sezona2_end = datetime(2021, 8, 31)


prijezd = datetime.strptime(input("Zadejte datum příjezdu DD.MM.YYYY: "), "%d.%m.%Y")
osoby = int(input("Zadejte počet osob: "))

if prijezd > sezona1_start:
    if prijezd < sezona2_end:
        if prijezd < sezona1_end:
            print(f"Cena je: {osoby*250} Kč.")
        elif prijezd > sezona1_end:
            print(f"Cena je: {osoby*180} Kč.")
else:
    print("Letní kino je v této době uzavřené.")




#print(prijezd)
#print(f"{sezona_start_1.day}/{sezona_start_1.month}/{sezona_start_1.year}")





