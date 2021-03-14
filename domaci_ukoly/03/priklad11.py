"""
Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:
Registrační značka 	Značka a typ vozidla 	Počet najetých kilometrů
4A2 3020 	        Peugeot 403 Cabrio 	    47534
1P3 4747 	        Škoda Octavia 	        41253

Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

    registrační značka automobilu,
    značka a typ vozidla,
    počet najetých kilometrů,
    informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- True pokud je volné a False pokud je vypůjčené).

Vytvoř funkci __init__ pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce __init__ a ulož je jako atributy objektu.
Poslední atribut nastav jako True, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.
"""

class Auta:
    def __init__(self, registr, znacka, ujeto):
        self.registr = registr
        self.znacka = znacka
        self.ujeto = ujeto
        self.volne = True

    def pujceno(self):
        self.volne = False

    def get_info(self):
        return f'Auto: {self.registr}, Značka a typ vozidla: {self.znacka}, Ujeto: {self.ujeto}, Volné: {self.volne}'

auto1 = Auta("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auta("1P3 4747", "Škoda Octavia", 441253)

auto2.pujceno()

print(auto1.get_info())
print(auto2.get_info())