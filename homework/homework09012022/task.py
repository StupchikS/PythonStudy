class Temperature:
    count = 0

    @staticmethod
    def f_to_c(num):
        if num < -459.4:
            return "температуры ниже обсолютного нуля физически нет"
        else:
            Temperature.count += 1  # считаю, что если прользователь ввел некорректно, то перевода не было
            return f"{num} по Фаренгейту равно {round((num - 32) / 1.8, 2)} по Цельсию"

    @staticmethod
    def c_to_f(num):
        if num < -273:
            return "температуры ниже обсолютного нуля физически нет"
        else:
            Temperature.count += 1
            return f"{num} по Цельсию равно {(num * 1.8) + 32} по Фаренгейту"

    @staticmethod
    def get_count():
        return Temperature.count


print(Temperature.get_count())
print(Temperature.f_to_c(-500))
print(Temperature.f_to_c(-70))
print(Temperature.c_to_f(-70))
print(Temperature.c_to_f(0))

print((Temperature.get_count()))
