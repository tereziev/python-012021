"""
Uvažuj program, který bude pracovat s výsledky z maturitní zkoušky. Každý student může mít jeden z následujících výsledků:

    "Prospěl s vyznamenáním", pokud je průměr jeho známek maximálně 1.5 a nemá žádnou trojku.
    "Neprospěl", pokud má alespoň jednu pětku.
    "Prospěl", pokud nemá vyznamenání a současně nedostal žádnou pětku.

Přidej funkci ohodnot_studenta(), která bude mít jeden parametr, kterým je slovník se známkami studenta.
Funkce rozhodne, zda student prospěl, prospěl s vyznamenáním nebo neprospěl podle výše popsaných kritérií.

Dále napiš cyklus, který projde seznam vysledky a pomocí funkce ohodnot_studenta() zjistí prospěch studenta.
Následně pro každého studenta vypíše jeho jméno a informaci o tom, zda prospěl, neprospěl či prospěl s vyznamenáním.

Výstup tvého programu by mohl vypadat např. takto:

Mirek Dušín: Prospěl s vyznamenáním
Jarka Metelka: Neprospěl
Jindra Hojer: Prospěl
Červenáček: Prospěl s vyznamenáním
Rychlonožka: Prospěl
"""

vysledky = [
  {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
  {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
  {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
  {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
  {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]

import math

soucet_znamek = {}
for student in vysledky:
    jmeno = student["Jméno"]
    znamky = student.pop("Jméno")
    znamky = list(student.values())
    #prumer = sum(znamky) / len(znamky)
    #print(f"{jmeno} má {prumer}.")
    if jmeno in soucet_znamek:
        soucet_znamek[jmeno] += znamky
    else:
        soucet_znamek[jmeno] = znamky

"""
print(soucet_znamek)
for jmeno, znamky in soucet_znamek.items():
    print(sum(znamky)/len(znamky))
"""

def ohodnot_studenta(soucet_znamek):
    prumer = sum(znamky)/len(znamky)
    if 5 not in znamky:
        if 3 not in znamky:
            if prumer <= 1.5:
                hodnoceni = 'Prospěl/a s vyznamenáním'
            else:
                hodnoceni = 'Prospěl/a'
        else:
            hodnoceni = 'Prospěl/a'
    else:
        hodnoceni = 'Neprospěl/a'
    return hodnoceni

for jmeno, znamky in soucet_znamek.items():
    print(f" {jmeno} : {ohodnot_studenta(student)}")
