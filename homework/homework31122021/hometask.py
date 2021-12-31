import math


class Sphere:

    def __init__(self, x=1, y=1, z=1):
        if Sphere.__is_digital(x):
            self.__x = x
        if Sphere.__is_digital(y):
            self.__y = y
        if Sphere.__is_digital(z):
            self.__z = z
        self.__r = 1  # таким образом я защитился, если сразу введут неправильный радиус, программа ложится

    def __is_digital(num):
        if isinstance(num, int) or isinstance(num, float):
            return True
        else:
            return False

    def set_centre(self, x, y, z):
        if Sphere.__is_digital(x):
            self.__x = x
        if Sphere.__is_digital(y):
            self.__y = y
        if Sphere.__is_digital(z):
            self.__z = z

    def set_radius(self, r):
        if Sphere.__is_digital(r) and r > 0:
            self.__r = r
        else:
            print("Радиус введен не правильно")

    def get_centre(self):
        return self.__x, self.__y, self.__z

    def get_radius(self):
        return self.__r

    def get_square(self):
        return round(4 * self.__r * self.__r * math.pi, 2)

    def get_volume(self):
        return round(4 * math.pi * self.__r ** 3 / 3, 2)

    def is_point_inside(self, x, y, z):
        if Sphere.__is_digital(x) and Sphere.__is_digital(y) and Sphere.__is_digital(z):
            if (x - self.__x)**2 + (y-self.__y)**2 + (z-self.__z)**2 > self.__r**2:
                return False
            else:
                return True
        else:
            print("Введены неправильные координаты")
            return None


p1 = Sphere()
p1.set_radius("0.6")
print(p1.get_radius())
print(p1.get_volume())
print(p1.get_square())
p1.set_centre(0, 0, 0)
print(p1.get_centre())
print(p1.get_square())
print(p1.is_point_inside(0, -1.5, 0))
p1.set_radius(1.6)
print(p1.get_radius())
print(p1.is_point_inside(0, -1.5, 0))
