"""
Uvažujme nyní opět třídu Employee, kterou jsme si ukázali v lekci.
Pro zjednodušení nyní nebudeme pracovat s dovolenou, proto nám stačí třída, která je v ukázce níže.

class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position):
    self.name = name
    self.position = position

Nyní se budeme zabývat platem. Přidej třídě atribut salary (výše hrubého platu) a children (počet dětí),
jehož výši nastavíš ve funkci __init__(). Dále přidej funkci get_net_salary(), která vypočte a vrátí výši čisté mzdy.
Uvažuj zjednodušený výpočet: sazba daně je 15 % a sleva na jedno dítě 1500 Kč.
Vzorec pro výpočet daně tedy je: daň = hrubá mzda * 0.15 - počet dětí * 1500. Funkce vrátí výši čisté mzdy, tj. čistá mzda = hrubá mzda - daň.
"""

class Employee:
    def get_net_salary(self):
        tax = self.salary * 0.15 - self.children * 1500
        net_salary = int(self.salary - tax)
        return net_salary
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}."
    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children

milos = Employee("Miloš Forman", "režisér", 50000, 3)
tim = Employee("Tim Burton", "režisér", 50000, 0)

print(milos.get_net_salary())
print(tim.get_net_salary())