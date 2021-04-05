"""
Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracovala pokročilou variantu, můžeš pracovat s teplotami ve stupních Celsia.

Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky. Dále napiš následující dotazy:

    Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
    Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US).
    Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
    Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.

"""
import pandas
import pytemperature

teploty = pandas.read_csv("temperature.csv")
teploty["AvgTemperatureCelsia"] = pytemperature.f2c(teploty["AvgTemperature"])

#print(teploty.columns)
#print(teploty.head(5))


print(f"#1 DOTAZ NA MĚŘENÍ 13.LISTOPADU:")
listopad13 = teploty[(teploty["Day"] == 13)]
print(listopad13[["City", "Day", "AvgTemperatureCelsia"]])
#vypisuju si jen některé sloupce z vlastní iniciativy - nevejdou se mi všechny sloupce na obrazovku, takže mi je pycharm zkrátí ...
print("---")


print(f"#2 DOTAZ NA MĚŘENÍ 13.LISTOPADU USA:")
usa_listopad13 = listopad13[listopad13["Country"] == "US"]
print(usa_listopad13[["Country","City", "Day", "AvgTemperatureCelsia"]])
print("---")

print(f"#3 DOTAZ NA MĚŘENÍ 13.LISTOPADU USA - Washington A Philadelphia:")
wash_phil = usa_listopad13[usa_listopad13["City"].isin(["Washington", "Philadelphia"])]
print(wash_phil[["Country", "City", "Day", "AvgTemperatureCelsia"]])
#proč tam je Washington dvakrát?
