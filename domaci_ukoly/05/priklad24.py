"""
Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.

Dále napiš následující dotazy:

    Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.
    Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
    Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
    Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
"""
import wget
import pandas

teploty = pandas.read_csv("temperature.csv")

#print(teploty.head(20))
#print("Teplota je pravděpodobně ve Fahrenheitech")


print(f"#1 DOTAZ NA MĚŘENÍ V PRAZE:")
praha = teploty[(teploty["City"] == "Prague")]
print(praha)
print("---")

print(f"#2 DOTAZ NA MĚŘENÍ, KDE JE TEPLOTA > 80 STUPŇŮ:")
vedro = teploty[(teploty["AvgTemperature"] > 80)]
print(vedro)
print("---")

print(f"#3 DOTAZ NA MĚŘENÍ, KDE JE TEPLOTA V EVROPĚ > 60 STUPŇŮ:")
evropa = teploty[teploty["Region"].isin(["Europe"])]
evropa_60 = evropa[(evropa["AvgTemperature"] > 60)]
print(evropa_60)
print("---")

print(f"#4 DOTAZ NA EXTRÉMNÍ HODNOTY:")
extrem = teploty[(teploty["AvgTemperature"] < -20) | (teploty["AvgTemperature"] > 80)]
print(extrem)
print("---")
#ve vypisu jsou i negativni hodnoty, jen bohužel nejsou v horních ani dolních 5, takže nejsou vidět

"""
Pokročilá varianta

Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia.
Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek.
Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

import pytemperature
df["AvgTemperatureCelsia"] = pytemperature.f2c(df["AvgTemperature"])

Nyní můžeš zpracovat následující příklady:

    Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
    Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
    Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?
"""
import pytemperature
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

print(f"#5 DOTAZ NA MĚŘENÍ, KDE JE TEPLOTA > 30 STUPŇŮ:")
vedro_C = teploty[(teploty["AvgTemperatureCelsia"] > 30)]
print(vedro_C)
print("---")

print(f"#6 DOTAZ NA MĚŘENÍ, KDE JE TEPLOTA V EVROPĚ > 60 STUPŇŮ:")
evropa = teploty[teploty["Region"].isin(["Europe"])]
evropa_15 = evropa[(evropa["AvgTemperatureCelsia"] > 15)]
print(evropa_15)
print("---")

print(f"#7 DOTAZ NA EXTRÉMNÍ HODNOTY:")
extrem = teploty[(teploty["AvgTemperatureCelsia"] < -10) | (teploty["AvgTemperatureCelsia"] > 30)]
print(extrem)
print("---")
