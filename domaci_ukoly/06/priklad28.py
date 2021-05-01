#STATY SVETA POTRETI
"""
import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
Zkusme nyní zpracovat podobné úlohy pomocí pandas.

    *   Načti data ze souboru do tabulky.
    *   Vyfiltruj státy, které leží v Evropě.
    *   Zjisti počet států v jednotlivých subregionech Evropy.
    *   Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
"""
import pandas


staty = pandas.read_json("staty.json")
#staty = staty.set_index("name")
print(staty.columns)
"""
#Vyfiltruj státy, které leží v Evropě:
print(staty[staty['region'] == "Europe"])

#Zjisti počet států v jednotlivých subregionech Evropy.
print(staty.groupby('subregion')["name"].count())

#Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.
print(staty.groupby('subregion')["population"].sum())
"""


"""
Rozšíření zadání

V souboru staty.json jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali.
V souboru gdp.csv jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP) států za roky 2017-2019 ze Světové banky.

    *   Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP
        (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
    
    *    Propoj obě tabulky podle třípísmenného kódu států.
    
    *    Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
    
        Projdi si subkapitolu o počítaných sloupcích (část o podmínených sloupcích není nutné číst).
        K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele,
        tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.

"""
#Jen státy s kompletním GDP za tři roky:
gdp = pandas.read_csv("gdp.csv")
#print(gdp.head())
gdp.dropna()
#print(gdp.columns)

#Propoj obě tabulky podle třípísmenného kódu států. -> musím nejdříve sjednotit pojmenování
gdp.rename(columns={"Country Code":"alpha3Code"}, inplace = True)

#print(gdp.columns)
staty_gdp = pandas.merge(staty, gdp, on="alpha3Code")
print(staty_gdp.columns)

#Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
staty_gdp_2019 = staty_gdp.groupby(['subregion']).agg({'2019':['sum'], 'population':['sum']})
print(staty_gdp_2019)

#K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele,
staty_gdp_2019["GDP_na_obvyatele"] = staty_gdp_2019["2019"] / staty_gdp_2019["population"]
print(staty_gdp_2019.head(5))