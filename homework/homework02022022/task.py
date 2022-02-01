class ValidTriangle:
    def __set_name__(self, owner, name):

        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f" {self.__name} должно быть интовым числом")
        if value <= 0:
            raise ValueError(f"Значение сторон должно быть положительным")
        instance.__dict__[self.__name] = value


class Triangle:
    a1 = ValidTriangle()
    a2 = ValidTriangle()
    a3 = ValidTriangle()

    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def is_triangle(self):
        if (self.a1 + self.a2) > self.a3 and (self.a1 + self.a3) > self.a2 and (self.a3 + self.a2) > self.a1:
            print(f" треугольник со сторонами {self.a1}, {self.a2} и {self.a3} существует")
        else:
            print(f" треугольник со сторонами {self.a1}, {self.a2} и {self.a3} не существует")


p1 = Triangle(2, 5, 6)
p2 = Triangle(5, 2, 8)
p3 = Triangle(7, 3, 6)
c = [p1, p2, p3]
for i in c:
    i.is_triangle()




