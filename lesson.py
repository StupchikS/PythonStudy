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


