import random as r

# h, w = 6, 6
# m = [[r.randint(0, 10) for x in range(w)] for y in range(h)]
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# row = 0
# while row < h:
#     m[row], m[row + 1] = m[row + 1], m[row]
#     row += 2
#
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# from math import *
#
# select = int(input("выбор фигуры 1 треугольник, 2 прямоугольник, 3 круг "))
# if select == 3:
#     radius = int(input("введите радиус "))
#     print("площадь круга ", round((pi * (radius ** 2)), 2))
# elif select == 2:
#     a = int(input("сторона 1 "))
#     b = int(input("сторона 2 "))
#     print("площадь прямоугольника ", a * b)
# elif select == 1:
#     a = int(input("сторона 1 "))
#     b = int(input("сторона 2 "))
#     c = int(input("сторона 3 "))
#     p = (a + b + c) / 2
#     print("площадь треугольника ", round(sqrt(p * (p - a) * (p - b) * (p - c)), 2))
# else:
#     print("error")

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("сегодня: %B %d, %Y"))

# d


# def get_sum(a, b):
#     if a < b:
#         return a + b
#     else:
#         return a - b
#
#
#
# x = int(input("1 namber "))
# y = int(input("2 namber "))
# print(get_sum(x, y))

# def cub(a):
#     return a ** 3
#
#
# i = 1
# while i < 11:
#     print(i, "в кубе = ", cub(i))
#     i += 1
#
#
# a = n
# a = b
# b = b + n

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["c", "l", "o", "n"]))


# def set_params(n=20, s="_"):
#     print(s*n)
#
#
# set_params(5, "!")
# set_params(10, "+")
# set_params()
# print(tuple(2**i for i in range(1, 13)))
# def slicer(tp, a):
#     if a in tp:
#         start = tp.index(a)
#         stop = tp.index(a, start + 1) + 1
#
#         return tuple(tp[start + 1:stop])
#     else:
#         print("нет", a, "в кортеже")

# def slicer(tup, num):
#     if num in tup:
#         if tup.count(num) > 1:
#             i1 = tup.index(num)
#             i2 = tup.index(num, i1 + 1) + 1
#             return tup[i1:i2]
#         else:
#             return tup[tup.index(num):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# def rond1(lst):
#     lstnew = []
#     lstr = lst[::-1]
#     for i in lstr:
#         if i not in lstnew:
#             lstnew.append(i)
#
#     return lstnew
#
#
# print(tuple(rond1([1, 2, 3, 3, 2])))
# print(tuple(rond1([2, 5, ])))


# a = {1, 2}
# c = {3}
# b = {4, 5}
# d = {3, 2, 6}
# i = {6}
# j = {6, 8}
# k = {9, 8}
# res = set()
# res =a | b | c | d | i | j | k
# print(res, len(res), max(res), min(res))

#


# a = "Python"
# b = "Programming language"
# aset = set(a)
# bset = set(b)
# print(aset - bset)


# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# k = 1
# for i in d:
#     k = k * d[i]
# print(k)

# d = {i: input("введите овощь ") for i in range(1, 5)}
# print(d)
# kdel = int(input("какой удалить "))
# del d[kdel]
# print(d)


# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# z = x.copy()
# z.update(y)
# print(z)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "new York"}
#
# d1 = dict()
# d1 = d.copy()
# del d1["age"]
# del d1["city"]
#
# print(d)
# print(d1)
# c = d ^ d1
# print(c)

# d = {"name": "Kelly", "age": 25, "salary": 8000, "city": "new York"}
# print(d)
# d["location"] = d.pop("city")
# print(d)


# sales = {"john": {"n": 3056, "s": 8456, "e": 8441, "w": 2694},
#      "tom": {"n": 4566, "s": 8456, "e": 8441, "w": 2694},
#      "anna": {"n": 1226, "s": 8456, "e": 891, "w": 2694},
#      "fiona": {"n": 3056, "s": 686, "e": 8441, "w": 2694}}
#
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep="")
#
#
# name = input("name ")
# region = input("code region ")
# num = int(input("numbers "))
#
# sales[name][region] = num
# print(sales[name])

# d = {"x1": 1, "x2": 2, "x3": 3, "x4": 4}
# d1 = {key: v for key, v in d.items() if v <= 2}
# print(d1)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         s = i
#         d[i] = []
#     else:
#         d[s].append(i)
# print(d)
# def ch(*argm):
#     a =[]
#     chnum = round(sum(argm) / len(argm), 2)
#     for i in argm:
#         if i < chnum:
#             a.append(i)
#     return chnum, a
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
# def reverse(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     if only_odd:
#         for i in args:
#             if i % 2 == 0:
#                 res.append(reverse(i))
#     else:
#         for i in args:
#             res.append(reverse(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5678, 62, 747, 81, 91))
# print(func(12, 2345, 323, 4456, 5678, 62, 747, 81, 91, only_odd=True))


# def func(**args):
#     d = {k: v for k, v in args.items()}
#     return d
#
#
#
# d = dict()
# print(func(one="first"))
# print(func(two="second"))


# def fn1(str):
#     n = 0
#     def fn():
#         nonlocal n
#         n += 1
#         print(str, n)
#
#     return fn
#
#
# res = fn1("Москва")
# res()
# res()
# res2 = fn1("Sochi")
# res2()
# res2()
# res()

# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))


# d = {
#     "circle": lambda r: print("s = ", 3.14 * r**2),
#     "rectangle": lambda x, y: print("s = ", x * y),
#     "trapezoid": lambda x, y, h: print("s = ", (x + y) * h / 2)
# }
#
# d["circle"](2)

# print((lambda x, y, z: x if x < y and x < z else y if y < x and y < z else z)(9, 8, 5))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))


# m = [r.randint(1, 40) for x in range(10)]
# print(m)
# print(list(filter(lambda s: 20 >= s >= 10, m)))


# i = 0
#
#
# def decor(fn):
#     i = 0
#     def wrap():
#         global i
#         # nonlocal i
#         i += 1
#         fn()
#         return i
#
#     return wrap
#
#
# @decor
# def hello():
#     print("Hello")
#
#
#
#
# print(hello())
# print(hello())
# print(hello())
#
# hello()
#


# def fun_dec(num):
#     def fun_fun(fn):
#         def wrap(n):
#             return (fn(n)) * num
#
#         return wrap
#
#     return fun_fun
#
#
# @fun_dec(3)
# def aaa(x):
#     return x
#
#
#
# print(aaa(5))
# def change_text(s, c_old, c_new):
#     #   return s.replace(c_old, c_new)
#     s2 = ""
#     for i in s:
#         if i == c_old:
#             s2 += c_new
#         else:
#             s2 += i
#     return s2
#
#
#
# str1 = "я изучаю Nython, мне Nython нравится"
#
# print(change_text(str1, "N", "P"))

# print(ord("s"))

# str1 = "Test string for me"
# codes = []
# arif_sum = 0
# for i in str1:
#     codes.append(ord(i))
#     arif_sum += ord(i)
# arif_sum = round(arif_sum/len(str1))
# codes.insert(0, arif_sum)
# print(codes)

# a = "hello world"
# s = a.find(" ")
# b = a[s:]
# b = b + " " + a[:s]
# print(b)

# s = "ab12c59p7dq"
# digits = []
# for i in s:
#     if i in "0123456789":
#         digits.append(int(i))
#
# print(digits)

# a = "Send unlimited free texts and make WiFi calls from a free phone number."
# f = "f"
# if f in a:
#     if a.find(f) != a.rfind(f):
#         print(a[a.find(f) + 1: a.rfind(f)])

# a = input("введите строку")
# inic = a.split()
# inic2 = "*".join(inic)
# print(inic2)
import re

# s = "Я ищу совпадения в 2021. И я их найду в 2 счета 16:24, 25:71"
# req =r"[0-2][0-9][:][0-5][0-9]"
# print(re.findall(req, s))

# s = "05-03-1987 # data berdday"
# print("дата рождения: ", re.sub(r'-', ".", re.sub(r"#.*", "", s)))

# text = "1234@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# #  reg = r"[a-z0-9а-я@\.\-_]{5,20}"  # my variant
# reg = r"[\w.-]+@[\w.]+\w{2,3}"
# print(re.findall(reg, text, re.I))

# text = "[34] thhj khhghf [78] [67] gfnhmk,nbbn vngnmjcxxv nhjm67u7ih [45]"
#
# reg = r"\[[0-9]+]"
# # her variant  r"\[.*?] но если добавить букву то тоже войдет [34h]
# print(re.findall(reg, text))

# d = "28-08-2021"
# reg = r'([0-3][0-9]|3[01])-(0[1-9]|1[0-2])-(202[0-9])'
# print(re.findall(reg, d))

# s = "google.com and google.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))


# def sum_list(lst):
#
#     if len(lst) == 1:
#
#         return lst[0]
#     return lst[0] + sum_list(lst[1:])
#
#
#
#
# print((sum_list([1, 3, 5, 7, 9])))
#
#
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]

# lst = [r.randint(0, 10) for i in range(10)]
#
#
# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#     while first <= last and not found:
#         mid = (first + last) // 2
#         if s[mid] == item:
#             found = True
#         else:
#             if item < s[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#
#     return found

#
#
# print("число есть" if binary_search(sorted(lst), int(input("-> "))) else "числа нет")
# print(lst)


# def lin_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#
#     return found
#
#
# def bubble(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - i - 1):
#             if var_sort == 1:
#                 if arr[j] > arr[j+1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             if var_sort == 2:
#                 if arr[j] < arr[j+1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
#
# a = [10, 12, 7]
# b = [5, 9, 6, 7]
# c = [2, 4]
# e = [10, 1, 12]
# var_sort = int(input("1 по возрастанию и 2 по убыванию "))
#
# lst = a + b + c + e
# if var_sort == 1 or var_sort == 2:
#     print(lst)
#     bubble(lst)
#     print(lst)
#     print("число есть" if lin_search(lst, int(input("что ищем -> "))) else "числа нет")
# else:
#     print("неправильный вариант")


# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif not left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#
#     return res
#
#
# array = [8, 2, 6, 4, 5]
# print(merge_sort(array))
#
# def merge_sort2(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [8, 2, 6, 4, 5]
# # array = [randint(1, 99) for i in range(10000)]
# print(array)
#
# array = merge_sort2(array)
# print(array)
#

# f = open('text.txt', 'r')
# count = 0
# for line in f:
#     count +=1
# f.close()
# print(count)


# f = open("text.txt", 'r')
# text_data = f.readlines()
# f.close()
# index_del = int(input("какую строку удаляем "))
# if index_del > len(text_data):
#     print("нет такой строки")
# else:
#     f = open("text.txt", 'w')
#     for i in range(len(text_data)):
#         if i == index_del - 1:
#             text_data[i] = ""
#     f.writelines(text_data)
# f.close()


import os
import os.path

# for path, names, files in os.walk("work", topdown=False):
#     if not names and not files:
#         os.rmdir(path)
#         print(path, "deleted")

# file_yes = "text1.txt"
# file_no = "text22.txt"
#
# if os.path.exists(file_no):
#     pass
# else:
#     print("111")


# class AutoClass:
#     marka_auto = "marka"
#     year_auto = "0000"
#     fabryc_auto = "fabryc"
#     power_auto = ""
#     color_auto = ""
#     price_auto = ""
#
#     def print_auto_class(self):
#         print(" Information about auto".center(40, "*"))
#         print(
#             f"Название модели: {self.marka_auto} \nГод выпуска: {self.year_auto} \nПроизводитель: {self.fabryc_auto} \n"
#             f"Мощность: {self.power_auto} \nЦвет машины: {self.color_auto} \nЦена: {self.price_auto}")
#         print("=" * 40)
#
#     def info_auto_class(self, marka, year, fabryc, power, color, price):
#         self.marka_auto = marka
#         self.year_auto = year
#         self.fabryc_auto = fabryc
#         self.power_auto = power
#         self.color_auto = color
#         self.price_auto = price
#
#     def set_marka(self, marka):
#         self.marka_auto = marka
#
#     def set_year(self, year):
#         self.year_auto = year
#
#     def set_fybryc(self, fabryc):
#         self.fabryc_auto = fabryc
#
#     def set_power(self, power):
#         self.power_auto = power
#
#     def set_color(self, color):
#         self.color_auto = color
#
#     def set_price(self, price):
#         self.price_auto = price
#
#     def get_marka(self):
#         return self.marka_auto
#
#     def get_year(self):
#         return self.year_auto
#
#     def get_fybryc(self):
#         return self.fabryc_auto
#
#     def get_power(self):
#         return self.power_auto
#
#     def get_color(self):
#         return self.color_auto
#
#     def get_price(self):
#         return self.price_auto
#
#
# auto1 = AutoClass()
# auto1.print_auto_class()
# auto1.info_auto_class("X5", "2021", "BMW", "530", "белый", "107345")
# auto1.print_auto_class()
# auto2 = AutoClass()
# auto2.set_year("2020")
# auto2.set_price("123678")
# auto2.set_marka("X7")
# auto2.set_fybryc("BMW")
# auto2.set_color("red")
# auto2.set_power("320")
# auto2.print_auto_class()
# print(auto2.get_year())
# print(auto1.get_year())


# class Kgfunt:
#
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg_funt(self):
#         return self.__kg * 2.205
#
#     @kg_funt.setter
#     def kg_funt(self, kg):
#         if type(kg) == int or type(kg) == float:
#             self.__kg = kg
#
#
# p1 = Kgfunt(10)
# print(p1.kg_funt)
# p1.kg_funt = 20
# print(p1.kg_funt)

# class Mat:
#     @staticmethod
#     def max_im(a, b, c, d):
#         maxn = a
#         if b > maxn:
#             maxn = b
#         if c > maxn:
#             maxn = c
#         if d > maxn:
#             maxn = d
#         return maxn
#
#     @staticmethod
#     def min_im(a, b, c, d):
#         minn = a
#         if b < minn:
#             minn = b
#         if c < minn:
#             minn = c
#         if d < minn:
#             minn = d
#         return minn
#
#     @staticmethod
#     def mid_arif(a, b, c, d):
#         return round((a + b + c + d) / 4, 2)
#
#     @staticmethod
#     def factorial(a):
#         res = 1
#         for i in range(1, a + 1):
#             res *= i
#         return res
#
#
# print(Mat.max_im(3, 5, 7, 9))
# print(Mat.min_im(3, 5, 7, 9))
# print(Mat.mid_arif(3, 5, 7, 9))
# print(Mat.factorial(5))


from abc import ABC, abstractmethod

# class Clock:
#     __DAY = 86400  # 24*60*60 - число секунд в одном дне
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.secs % 60  # секунды
#         m = (self.secs // 60) % 60  # минуты
#         h = (self.secs // 3600) % 24  # часы
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise AttributeError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.secs + other.secs)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise AttributeError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.secs + other.secs)
#
#     def __eq__(self, other):
#         return self.secs == other.secs
#
#     def __ne__(self, other):
#         return self.secs != other.secs
#
#     def __lt__(self, other):
#         return self.secs < other.secs
#
#     def __le__(self, other):
#         return self.secs <= other.secs
#
#     def __gt__(self, other):
#         return self.secs > other.secs
#
#     def __ge__(self, other):
#         return self.secs >= other.secs
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = Clock(300)
# print(c3.get_format_time())
# # c4 = c1 + c2 + c3
# c1 += c2 + c3  # c1 = c1 + c2
# print(c1.get_format_time())

#
# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Операнд должен быть экземпляром класса"
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, (int, float))
#
#     @staticmethod
#     def __check0(ex):
#         if ex.x == 0 or ex.y == 0 or ez == 0:
#             raise ZeroDivisionError("на ноль делить нельзя")
#
#     def __str__(self):
#         return f"{self.__x}, {self.__y}, {self.__z}"
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.__x, self.__y * other.__y, self.__z * other.__z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.__x, self.__y / other.__y, self.__z / other.__z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return Point3D(self.__x == other.__x, self.__y == other.__y, self.__z == other.__z)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("str nado")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("неверное значение ключа")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("str nado")
#         if self.__check_value(value):
#             if key == "x":
#                 self.__x = value
#             if key == "y":
#                 self.__y = value
#             if key == "z":
#                 self.__z = value
#         else:
#             print("координаты должны быть числами")
#
#
#
# pt = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f"координаты 1 точки {pt}")
# print(f"координаты 2 точки {pt2}")
# pt3 = pt + pt2
# print(pt3)
# pt3 = pt - pt2
# print(pt3)
# pt3 = pt * pt2
# print(pt3)
# print("x =", pt["x"], "x2 =", pt2["x"])
# pt["x"] = 20
# print(pt)


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}, мне {self.age}"
#
#     def sound(self):
#         return f"{self.name} мявкает"
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я пес. Меня зовут {self.name}, мне {self.age}"
#
#     def sound(self):
#         return f"{self.name} гавкает"
#
#
# d1 = Dog("Мухтар", 4)
# d2 = Cat("Пушок", 2.5)
#
# s = [d1, d2]
# for i in s:
#     print(i.info())
#     print(i.sound())
#
#
# class Message:
#     _REGISTRY = {}
#     def __init__(self, text):
#         self.text = text
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTRY[name] = klass
#             return klass
#         return decorator
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTRY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенджера нет.")
#         print(text, end=" ")
#         return klass(text)
#
# @Message.register('Telegram')
# class TelegramMessage(Message):
#     def send(self):
#         print("(Telegram)")
#
# @Message.register('WhatsApp')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(WhatsApp)")
#
# @Message.register('Viber')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(Viber)")
#
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create("WhatsApp", "new text")
# m2.send()
# m3 = Message.create("Viber", "text new text")
# m3.send()


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"error {self.__name}")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("ivan", "Petrov")
# print(p.name)
# print(p.surname)
# p.name = "Vala"
# print(p.name)

# def isinstance(value, int):
#     pass
#
#
# class ValueError:
#     pass
#
#
# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if isinstance(value, int) and value > 0:
#             instance.__dict__[self.__name] = value
#         elif isinstance(value, str):
#             instance.__dict__[self.__name] = value
#         else:
#             raise ValueError(f"error {self.__name} or {self.__name} < 0")
#
#
#
# class Order:
#     name = ValidString()
#     price = ValidString()
#     count = ValidString()
#
#     def __init__(self, name, price, count):
#         self.name = name
#         self.price = price
#         self.count = count
#
#     def send(self):
#         return self.count * self.price
#
#
# p = Order("Apple", 5, 10)
# print(p.name)
# print(p.price)
#
# print(p.count)
# print(p.send())
# p2 = Order("pens", 5, -10)
# print(p2.send()

# from bs4 import BeautifulSoup
#
#
# # def get_copywriter(tag):
# #     whois = tag.find("div", class_="whois")
# #     if "Copywriter" in whois:
# #         return tag
# #     return None
#
#
# f = open("index.html", encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find_all("div", class_="row")[1].find_all("div", class_="links")
# # row = soup.find_all("div", {"class": "name"})
# # row = soup.find("div", text="Alena").find_parent(class_="row")
# # row = soup.find("div", id="whois3").find_next_siblings()
# # row = soup.find("div", id="whois3").find_previous_siblings()
# # print(row)
# # copiwriter = []
# # row = soup.find_all("div", class_="row")
# # for i in row:
# #     cw = get_copywriter(i)
# #     if cw:
# #         copiwriter.append(cw)
# # print(copiwriter)
#
#
# # поиск всех зарплат
#
# def get_salary(s):
#     pattern = r"\d+"
#     res = re.findall(pattern, s)[0]
#     print(res)
#
#
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)
# # print(salary)


import requests
from bs4 import BeautifulSoup
import subprocess
import csv

#
# rr = requests.get("https://ru.wordpress.org/")
# print(rr.text)


def get_html(url):
    rr = requests.get(url)
    return rr.text


def refined(s):
    res = re.sub(r"[\D+]", "", s)
    return res


def write_csv(data):
    with open("plagins.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(data["name"])


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    p1 = soup.find_all("section", class_="plugin-section")[1]
    plugins = p1.find_all("article")
    for i in plugins:
        name = i.find("h3").text
        url = i.find("h3").find("a").get("href")
        rating = i.find("span", class_="rating-count").find("a").text
        rei = refined(rating)
        print(name)
        print(url)
        print(rating)
        print(rei)
        # data = {"name": name, "url": url1, "rating": rei}
        # write_csv(data)



def main():
    url = "https://ru.wordpress.org/plugins/"
    get_data(get_html(url))


if __name__ == "__main__":
    main()

