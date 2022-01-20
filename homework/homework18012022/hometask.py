import math
from abc import ABC, abstractmethod


class Koren(ABC):
    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    @abstractmethod
    def search_koren(self):
        print("Абстрактный метод search_koren должен быть в дочерних классах")


class Lineequation(Koren):
    def __init__(self, a, b):
        super().__init__(a, b)

    def search_koren(self):
        x = round(-self._b / self._a, 2)
        print(f"корень линейного уравнения {self._a}x + {self._b} = 0 равен {x}")


class Sqrdequation(Koren):

    def search_koren(self):
        d = self._b**2 - 4 * self._a * self._c
        x1 = round((-self._b + math.sqrt(d)) / (2 * self._a), 2)
        x2 = round((-self._b - math.sqrt(d)) / (2 * self._a), 2)
        print(f"корни квадратного уравнения {self._a}x^2  {self._b}x  {self._c} = 0 равны {x1} и {x2}")


p1 = Sqrdequation(1, -2, -3)
#  print(p1.__dict__)
p1.search_koren()
print()
p2 = Lineequation(3, 7)
#  print(p2.__dict__)
p2.search_koren()
