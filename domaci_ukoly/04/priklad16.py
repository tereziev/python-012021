"""
Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa.
Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry.
Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

    Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
    Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr.
        Oba atributy nastav ve funkci __init__(), žánr získej jako parametr funkce.
    Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
    Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
    Všem třídám přidej funkci get_info(), která vypíše informace o položce, resp. o filmu a seriálu.
        Funkce u třídy Polozka vypíše název a žánr.
        Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.

Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál o ověr, že vše funguje.
"""

class Polozka:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
    def get_info(self):
        return f' Název: {self.title}, žánr: {self.genre}'

class Film(Polozka):
    def __init__(self, title, genre, length):
        super().__init__(title, genre)
        self.length = length
    def get_info(self):
        return f' Film: {self.title}, žánr: {self.genre}, délka: {self.length} min.'

class Serial(Polozka):
    def __init__(self, title, genre, number_of_episodes, length_of_episode):
        super().__init__(title, genre)
        self.number_of_episodes = number_of_episodes
        self.length_of_episode = length_of_episode
    def get_info(self):
        return f' Seriál: {self.title}, žánr: {self.genre}, počet epizod: {self.number_of_episodes}, délka epizody: {self.length_of_episode} min.'

matrix = Film("Matrix", "akční", "136")
pratele = Serial("Přátelé", "sitcom", "200", "20")

print(matrix.get_info())
print(pratele.get_info())

#nevěděla jsem, co znamená: "žánr získej jako parametr funkce" :(
#určitě jde vytunit funkci "get_info" - aby nebylo třeba kopírovat?