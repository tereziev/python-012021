"""
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci.
Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.

    Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto,
    které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
    Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
    Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
    Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
    Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.

"""
import pandas

platy = pandas.read_csv("platy_2021_02.csv")
praha = pandas.read_csv("zam_praha.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
liberec = pandas.read_csv("zam_liberec.csv")
praha["město"] = "Praha"
plzen["město"] = "Plzeň"
liberec["město"] = "Liberec"

zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)

"""
print(f"Praha: {praha.shape}")
print(f"Plzeň: {plzen.shape}")
print(f"Liberec: {liberec.shape}")
print(f"Všechna města: {all_mesta.shape}")
"""

#obe tabulky maji cislo_zamestnance -> merguju
zamestnanci_platy = pandas.merge(zamestnanci, platy, on="cislo_zamestnance")
print(zamestnanci_platy.shape)
#Nová tabulka má už jen 43 řádků, tzn. vůči původním 56 už 13 zaměstnanců nemá plat za únor (pandas ho vynechal) - a ve firmě už nepracuje
## funkce merge() ve výchozím nastavení ponechá pouze řádky, které mají záznamy v obou tabulkách

#print(platy_unor.head(10))

# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích:
print(round(zamestnanci_platy.groupby('město')['plat'].mean()))

"""
Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují.
Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
"""

#uz_nepracuji = ... fce isnull, count

zamestnanci_platy2 = pandas.merge(platy, zamestnanci, how="right")
uz_nepracuji = zamestnanci_platy2[zamestnanci_platy2["plat"].isnull()]
uz_nepracuji_pocet = len(zamestnanci_platy2[zamestnanci_platy2["plat"].isnull()])
print(uz_nepracuji)
uz_nepracuji.to_csv()

