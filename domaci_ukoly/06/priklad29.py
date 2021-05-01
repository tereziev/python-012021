"""
TEPLOTA VE MĚSTECH POTŘETÍ

Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.

    *   Vyfiltruj si informace o teplotách 13. listopadu 2017.
    *   Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
    *   Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
    *   Vypočti průměrnou teplotu za jednotlivé regiony.
    *   Vypočti maximální a minimální teplotu v každém regionu.

"""
import pandas
import pytemperature

teploty = pandas.read_csv("temperature.csv")
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

#print(teploty.head())

#Vyfiltruj si informace o teplotách 13. listopadu 2017.
print(teploty[(teploty["Day"] == 13)])

#Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
chyba_index = teploty[teploty["AvgTemperature"] == -99].index
teploty.drop(chyba_index, inplace = True)

#Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
print(teploty.groupby(['Day', 'Region'])["AvgTemperature"].count())

#Vypočti průměrnou teplotu za jednotlivé regiony.
print(teploty.groupby('Region')["AvgTemperatureCelsia"].mean())

#Vypočti maximální a minimální teplotu v každém regionu.
print(teploty.groupby('Region').agg({"AvgTemperatureCelsia": ['min', 'max']}))






