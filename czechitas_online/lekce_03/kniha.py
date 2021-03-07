class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def discount(self, discount):
        self.price = self.price - (self.price / 100 * discount)

    def get_info(self):
        return f" Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."