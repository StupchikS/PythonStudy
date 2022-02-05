from homework.homework06022022.el_auto.electro import *

auto1 = Electro("Tesla", "S", 2018, 99000, 87)
auto2 = Electro("Tesla", "3", 2020, 19000, 95)
auto3 = Electro("Nissan", "Leaf", 2013, 195000, 103)  # моя конкретно машина, мне эта тема близка
auto4 = Electro("Mitsubishi", "I miev", 2011, 64000, 72)

d = [auto1, auto2, auto3, auto4]
for i in d:
    i.electro_info()