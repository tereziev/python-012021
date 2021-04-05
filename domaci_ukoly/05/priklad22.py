"""
Stáhni si soubor character-deaths.csv, který obsahuje informace o smrti některých postav z prvních pěti knih románové série Píseň ohně a ledu (A Song of Fire and Ice).

    Načti soubor do tabulky (DataFrame) a nastav sloupec Name jako index.
    Zobraz si sloupce, které tabulka má. Posledních pět sloupců tvoří zkratky názvů knih a informace o tom, jestli se v knize postava vyskytuje.
    Použij funkci loc ke zjištění informací o smrti postavy jménem "Hali".
    Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam".
    Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a sloupce Death Year.
    Použij funkci loc k zobrazení řádků mezi "Gevin Harlaw" a "Gillam" a informace o tom,
    v jakých knihách se postava vyskytuje, tj. vypiš všechny sloupce mezi GoT a DwD.

"""
import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")

deathlist = pandas.read_csv("character-deaths.csv")
deathlist = deathlist.set_index("Name")

print(f"#1 NAČTI SOUBOR A NASTAV INDEX = SLOUPEC 'NAME':")
print(deathlist.index)
print("---")

print(f"#2 ZOBRAZ SLOUPCE TABULKY:")
print(deathlist.columns)
print("---")

print(f"#3 INFO O SMRTI POSTAVY 'Hali':")
print(deathlist.loc["Hali"])
print("---")

print(f"#4 ZOBRAZ ŘÁDKY MEZI 'Gevin Harlaw' A 'Gillam':")
print(deathlist.loc["Gevin Harlaw":"Gillam"])
print("---")

print(f"#5 ZOBRAZ ŘÁDKY MEZI 'Gevin Harlaw' A 'Gillam', ZOBRAZ SLOUPEC 'Death Year':")
print(deathlist.loc["Gevin Harlaw":"Gillam", "Death Year"])
print("---")

print(f"#5 ZOBRAZ ŘÁDKY MEZI 'Gevin Harlaw' A 'Gillam', ZOBRAZ SLOUPCE KNIH:")
print(deathlist.loc["Gevin Harlaw":"Gillam", "GoT" : "DwD"])
print("---")