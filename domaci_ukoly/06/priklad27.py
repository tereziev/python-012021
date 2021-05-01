"""
import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty pro jednoho vybraného zákazníka.

    * Načti data ze souboru a ulož je do tabulky.

    * Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.

"""
import pandas

vykazy = pandas.read_csv("vykazy.csv")
#print(vykazy.head())

print(vykazy.groupby('project')["hours"].count())

"""
DOBROVOLNÝ DOPLNĚK:
    *   Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.

    *   Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře,
        tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
"""

platy = pandas.read_csv("platy_2021_02.csv")
praha = pandas.read_csv("zam_praha.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
liberec = pandas.read_csv("zam_liberec.csv")
praha["město"] = "Praha"
plzen["město"] = "Plzeň"
liberec["město"] = "Liberec"

#vykazy.rename(columns={"employee_id":"cislo_zamestnance"}, inplace=True)
zamestnanci = pandas.concat([praha, plzen, liberec], ignore_index=True)

zamestnanci.rename(columns={"cislo_zamestnance":"employee_id"}, inplace= True)
vykazy.rename(columns={"emloyee_id":"employee_id"}, inplace = True)
print(zamestnanci.columns)
print(vykazy.columns)


zamestnanci_vykazy = pandas.merge(zamestnanci, vykazy, on="employee_id")
#print(zamestnanci_vykazy.head(10))

#grouping by multiple columns
print(zamestnanci_vykazy.groupby(['project', 'město']).agg({'hours':['sum']}))

#priklad30:
zamestnanci_vykazy.to_excel('zamestnanci_vykazy.xlsx', index=False)

