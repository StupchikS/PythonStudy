class Automobil:
    def __init__(self, brand, model, year, odd):
        self.brand = brand
        self.model = model
        self.year = year
        self.odd = odd

    def auto_info(self):
        print(f"Автомобиль {self.brand} {self.model}, год выпуска {self.year}, пробег автомобиля {self.odd} км")
