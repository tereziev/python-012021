
prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    #"Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

book = input("Zadej název knihy: ")
total = 0

if book in prodeje2019:
    total += prodeje2019[book]
else:
    print(f"Kniha se v roce 2019 neprodávala.")
if book in prodeje2020:
    total += prodeje2020[book]
print(f"Knihy {book} se celkem prodalo {total} kusů.")