"""
Moduly v Pythonu se často snaží zpříjemnit život programátorům. Například je občas otrava vymýšlet jména nebo adresy, když chceme vyzkoušet, jestli náš program funguje.
Jindy třeba potřebujeme nějaká data anonymizovat, tj. odebrat z nich citlivé osobní údaje jako jména, adresy atd.
Pro tento účel existuje modul Faker, která nám umí vygenerovat jména, adresy a řadu dalších dat, které můžeme využít při testování našich programů.

Nainstaluj si modul Faker pomocí postupu, který jsme si ukazovali na cvičení a je popsán v příkladu 19.

Níže máš příklad použití modulu. Nejprve provedeme import modulu, následně vytvoříme objekt generator_falesnych_dat třídy Faker.
Využijeme parametr "cs_CZ", který řekne modulu, aby nám generoval česká jména a adresy.
Objekt generator_falesnych_dat má naprogramované funkce jako name() pro vygenerování náhodného jména, address pro vygenerování náhodné adresy atd.

from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

print(generator_falesnych_dat.name())
print(generator_falesnych_dat.address())

Pojďme si modul vyzkoušet. Níže je třída Balik, která se podobá třídě, kterou už jsme vytvářeli během lekce. Náš balík má příjemce a adresu.

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print("Balík doručte na adresu: " + self.address)

  def __init__(self, name, address):
    self.name = name
    self.address = address

Zkus nyní vytvořit nějaký objekt ze třídy Balik a přiřadit mu náhodně vygenerované jméno příjemce a adresu. Pomocí funkce get_info() si nech informace o balíku vypsat.
"""
from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

#print(generator_falesnych_dat.name())
#print(generator_falesnych_dat.address())

class Balik:
    def get_info(self):
        print(f"Příjemce balíku: {self.name}")
        print("Balík doručte na adresu: " + self.address)

    def __init__(self, name, address):
        self.name = name
        self.address = address

balik1 = Balik(generator_falesnych_dat.name(), generator_falesnych_dat.address())
balik1.get_info()
