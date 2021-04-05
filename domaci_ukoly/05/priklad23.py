"""
Stáhni si soubor country_vaccinations.csv o průběhu očkování proti nemoci COVID-19.

Dále napiš následující dotazy:

    Dotaz na počty očkovaných (sloupec total_vaccinations) v jednotlivých státech dne 2021-03-10
    (s datem pracuj úplně stejně jako s řetězcem, tj. nevyužívej modelu datetime, ale vlož do dotazu přímo řetězec).
    Dotaz na řádky, kde 2021-03-10 bylo naočkováno více než 1 mil. obyvatel.
    Podíváme se na extrémní hodnoty. Napiš dotaz na řádky, kde za daný den naočkování více než 100 tisíc lidí nebo naopak méně než 100 lidí.

"""
import wget
import pandas

vakcinace = pandas.read_csv("country_vaccinations.csv")

print(f"#1 DOTAZ NA POČET OČKOVANÝCH V JEDNOTLIVÝCH STÁTECH DNE 2021-03-10:")
den_10_3 = vakcinace[(vakcinace["date"] == "2021-03-10")]
print(den_10_3[["country", "total_vaccinations"]])
print("---")

print(f"#2 DOTAZ NA ŘÁDKY, KDE 2021-03-10 BYLO NAOČKOVÁNO VÍCE NEŽ 1 MIL. OBYVATEL:")
velke_ockovani = vakcinace[(vakcinace["date"] == "2021-03-10") & (vakcinace["total_vaccinations"] > 1_000_000)]
print(velke_ockovani[["country", "total_vaccinations"]])
print("---")

print(f"#3 EXTRÉMNÍ HODNOTY:")
extremni_hodnoty = den_10_3[(den_10_3["total_vaccinations"] > 100_000) | (den_10_3["total_vaccinations"] < 100_000)]
print(extremni_hodnoty[["country", "total_vaccinations"]])