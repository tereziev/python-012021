"""
Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů, které uživatel zhlédl.
Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).

Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.

Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty.
Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a),
kolik minut (nebo hodin) videa celkem uživatel zhlédl.

Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné
a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().
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
    def get_celkova_delka(self):
        zhlednuto = int(self.length)
        return zhlednuto

class Serial(Polozka):
    def __init__(self, title, genre, number_of_episodes, length_of_episode):
        super().__init__(title, genre)
        self.number_of_episodes = number_of_episodes
        self.length_of_episode = length_of_episode
    def get_info(self):
        return f' Seriál: {self.title}, žánr: {self.genre}, počet epizod: {self.number_of_episodes}, délka epizody: {self.length_of_episode} min.'
    def get_celkova_delka(self):
        zhlednuto = int(self.number_of_episodes * self.length_of_episode)
        return zhlednuto

class Uzivatel():
    def __init__(self,uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    def pripocti_zhlednuti(self, zhlednuto):
        self.delka_sledovani += zhlednuto
#        hodin = zhlednuto // 60
#        minut = zhlednuto % 60
    def get_info(self):
        return f'Uživatel {self.uzivatelske_jmeno} zhlédl celkem {self.delka_sledovani//60} hodin a {self.delka_sledovani%60} minut.'

matrix = Film("Matrix", "akční", "136")
pratele = Serial("Přátelé", "sitcom", "200", "20")
terez = Uzivatel("@tereziev")


terez.pripocti_zhlednuti(matrix.get_celkova_delka())
print(terez.get_info())