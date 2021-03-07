class Employee:
    def take_holiday(self, days):
        if self.holidays >= days:
            self.holidays = self.holidays - days
            # ==> funkce na čerpání dovolené
            return f"Dovolená schválena."
        else:
            return f"Můžeš si vzít pouze {self.holidays} dnů."

    def get_info(self):
        return(f"{self.name} pracuje na pozici {self.position}.")

    def __str__(self):
        return self.name + ", " + self.position + ", " + str(self.holidays)

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.holidays = 25

frantisek = Employee("František Novák", "konstruktér")
klara = Employee("Klára Nová", "konstruktérka")
print(frantisek)
print(frantisek.take_holiday(10))
print(frantisek.take_holiday(10))
print(frantisek.take_holiday(10))

"""
frantisek = Employee()
frantisek.name = "František Novák"
frantisek.position = "konstruktér"
print(frantisek.get_info())

klara = Employee()
klara.name = "Klára Nová"
klara.position = "konstruktérka"
print(klara.get_info())
"""