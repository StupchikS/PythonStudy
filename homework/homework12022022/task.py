import json


def write_json(data_new):
    try:
        data_old = json.load(open("data.json"))
    except FileNotFoundError:
        data_old = []
    data_old.append(data_new)
    with open("data.json", "w") as f:
        json.dump(data_old, f, indent=4)


def show_json():
    try:
        data_old = json.load(open("data.json"))
        print(data_old)
    except FileNotFoundError:
        print("Данных нет")





new_data = {}

while True:
    print(
        f"Выбор действия '\n' 1 - Добавление данных '\n' 2 - Удаление данных '\n' 3 - Поиск данных "
        f"'\n' 4 - Редактирование данных '\n' 5 - Сохранение данных '\n' 6 - Показать данные текущие '\n' "
        f"7 - Показать данные файла '\n' 8 - Выход")
    your_select = int(input("=> "))

    if your_select == 1:
        new_data[input("Введите страну ")] = input("Введите столицу ")

    if your_select == 2:
        a = input("Введите страну для удаления ")
        try:
            del new_data[a]
        except print("Нет такой страны"):
            pass

    if your_select == 3:
        a = input("Введите страну для поиска ")
        try:
            print(new_data[a])
        except print("Нет такой страны"):
            pass

    if your_select == 4:
        a = input("Введите страну для редактирования ")
        new_data[a] = input("Введите столицу ")

    if your_select == 5:
        write_json(new_data)
        new_data = {}

    if your_select == 6:
        print(new_data)

    if your_select == 7:
        show_json()

    if your_select == 8:
        break
