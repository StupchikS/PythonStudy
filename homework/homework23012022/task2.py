class Clock:
    __DAY = 86400  # 24*60*60 - число секунд в одном дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")
        self.secs = secs % self.__DAY
        self.__h = (self.secs // 3600) % 24
        self.__m = (self.secs // 60) % 60
        self.__s = self.secs % 60

    def get_format_time(self):
        s = self.secs % 60  # секунды
        m = (self.secs // 60) % 60  # минуты
        h = (self.secs // 3600) % 24  # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise AttributeError("Правый операнд должен быть типом данных Clock")
        return Clock(self.secs + other.secs)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise AttributeError("Правый операнд должен быть типом данных Clock")
        return Clock(self.secs + other.secs)

    def __eq__(self, other):
        return self.secs == other.secs

    def __ne__(self, other):
        return self.secs != other.secs

    def __lt__(self, other):
        return self.secs < other.secs

    def __le__(self, other):
        return self.secs <= other.secs

    def __gt__(self, other):
        return self.secs > other.secs

    def __ge__(self, other):
        return self.secs >= other.secs

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError("Индекс задается строкой")
        elif item == "hour":
            return Clock.__get_form(self.__h)
        elif item == "min":
            return Clock.__get_form(self.__m)
        elif item == "sec":
            return Clock.__get_form(self.__s)
        else:
            print("неверное значение ключа")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Индекс задается строкой")
        if isinstance(value, int):
            if key == "sec" and 0 <= value < 60:
                self.__s = value
            elif key == "min" and 0 <= value < 60:
                self.__m = value
            elif key == "hour" and 0 <= value < 23:
                self.__h = value
            else:
                print("неверное значение ключа или значение не удовлетворяет стандартам времени")
        else:
            print("значение должно быть целым числом")


c1 = Clock(100)
c2 = Clock(200)
print(c1["min"])
print(c1.get_format_time())

print(c2.get_format_time())
c3 = Clock(300)
print(c3.get_format_time())
c4 = c1 + c2 + c3
print(c4.get_format_time())
c1 += c2 + c3
print(c1.get_format_time())
print("*" * 40)

c5 = Clock(80000)
print(c5.get_format_time())
print(c5["hour"], c5["min"], c5["sec"])
print("*" * 40)
c5["hour"] = 10
print(c5.get_format_time())
print(c5["hour"], c5["min"], c5["sec"])
c5["sec"] = 55
print(c5["hour"], c5["min"], c5["sec"])
