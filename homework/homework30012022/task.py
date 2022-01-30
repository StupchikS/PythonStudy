from abc import ABC, abstractmethod

class Shape:
    def __init__(self, a1, color):
        self.a1 = a1
        self.color = color

    @abstractmethod
    def search_perimetr(self):
        raise ValueError("Абстрактный метод search_perimetr должен быть в дочерних классах")

    @abstractmethod
    def search_square(self):
        raise ValueError("Абстрактный метод search_square должен быть в дочерних классах")

    @abstractmethod
    def info(self):
        raise ValueError("Абстрактный метод info должен быть в дочерних классах")

    @abstractmethod
    def paint_shape(self):
        raise ValueError("Абстрактный метод paint_shape должен быть в дочерних классах")

class Scuare(Shape):
    def __init__(self, a1, color):
        super().__init__(a1, color)

    def search_perimetr(self):
        return self.a1 * 4

    def search_square(self):
        return self.a1 ** 2

    def info(self):
        return f"цвет квадрата со стороной {self.a1} {self.color}"

    def paint_shape(self):
        for i in range(self.a1):
            print("@" * self.a1)


class Rectangle(Shape):
    def __init__(self, a1, a2, color):
        super().__init__(a1, color)
        self.a2 = a2

    def search_perimetr(self):
        return (self.a1 + self.a2) * 2

    def search_square(self):
        return self.a1 * self.a2

    def info(self):
        return f"цвет прямоугольника со сторонами {self.a1} и {self.a2} {self.color}"

    def paint_shape(self):
        for i in range(self.a1):
            print("@" * self.a2)


class Triangle(Shape):
    def __init__(self, a1, a2, a3, color):
        super().__init__(a1, color)
        self.a2 = a2
        self.a3 = a3

    def search_perimetr(self):
        return self.a1 + self.a2 + self.a3

    def search_square(self):
        p = (self.a1 + self.a2 + self.a3) / 2
        return round((p * (p - self.a1) * (p - self.a2) * (p - self.a3)) ** 0.5, 2)

    def info(self):
        return f"цвет треугольника со сторонами {self.a1} и {self.a2} и {self.a3} {self.color}"

    def paint_shape(self):
        for i in range(self.a2):
            print(" " * i, "@" * (self.a1 - 2 * i), " " * i)



p1 = Scuare(3, "красный")
p2 = Rectangle(3, 7, "зеленый")
p3 = Triangle(11, 6, 6, "желтый")

p123 = [p1, p2, p3]
for i in p123:
    print(i.info())
    print(i.search_perimetr())
    print(i.search_square())
    i.paint_shape()


