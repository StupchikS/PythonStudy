class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val):
        self.density = val

    def calc_v(self, m):
        v = round(m / self.density, 6)  # С небольшимы числами объем в кубометрах равен почти нулю
        print(f"Объем {m} кг {self.name} равен {v} m^3")
        return v

    def calc_m(self, v):
        m = round(v * self.density, 1)  # Красивее так
        print(f"Масса {v} m^3 {self.name} равна {m} кг")
        return m


class Alcohol(Liquid):
    def __init__(self, name, density, fortress):
        self.fortress = fortress
        super(Alcohol, self).__init__(name, density)

    def edit_fortress(self, fortress):
        self.fortress = fortress


p1 = Alcohol("wine", 1064.2, 12)
p2 = Alcohol("vodka", 831, 40)
p3 = Alcohol("beer", 1000, 9)

p1.calc_m(12)
p2.calc_m(12)
p3.calc_m(12)
p1.calc_v(4)
print("change density")
p1.edit_density(1082.1)
p1.calc_v(4)
print(p3.name, p3.density, p3.fortress)
print("change fortress")
p3.edit_fortress(12)
print(p3.name, p3.density, p3.fortress)
