"""
Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.

Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry,
a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal.
Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden,
a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu
a ten vrať pomocí klíčového slova return.

Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel
a jak dlouho ho měl půjčené. Poté vypiš informaci o ceně.
"""

cena = 0

class Auta:
    def __init__(self, registr, znacka, ujeto):
        self.registr = registr
        self.znacka = znacka
        self.ujeto = ujeto
        self.volne = True

    def pujc_auto(self):
        if self.volne:
            self.volne = False
            return f"Potvrzuji zapůjčení vozidla {self.znacka}."
        else:
            return f"Vozidlo bohužel není k dispozici."

    def vrat_auto(self, tachometr, doba):
        self.tachometr = tachometr
        self.doba = doba
        self.ujeto = self.ujeto + tachometr
        self.volne = True
        if doba <= 7:
            cena = doba * 400
        elif doba > 7:
            cena = doba * 300
        return f"Cena za zapůjčení auta je {cena} Kč."

    def get_info(self):
        return f'Auto reg. zn.: {self.registr}, {self.znacka}, Ujeto: {self.ujeto}, Volné: {self.volne}'

auto1 = Auta("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auta("1P3 4747", "Škoda Octavia", 441253)

dotaz_pujceni = input("Jaké auto si přejete zapůjčit? Škoda / Peugeot: ")

if dotaz_pujceni == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
elif dotaz_pujceni == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
else:
    print(f"Neplatný požadavek.")

dotaz_vraceni = input("Jaké auto si přeje vrátit? Škoda / Peugeot: ")
tachometr = int(input("Kolik kilometrů jste najeli: "))
doba = int(input("Kolik dní jste měli auto půjčené: "))

if dotaz_vraceni == "Škoda":
    print(auto2.vrat_auto(tachometr, doba))
    print(auto2.get_info())

elif dotaz_vraceni == "Peugeot":
    print(auto1.vrat_auto(tachometr, doba))
    print(auto1.get_info())

else:
    print(f"Neplatný požadavek.")