import json
from random import choice


def get_person():
    name = ""
    tel = ""
    nums = ""
    person = []
    letters = ["a", "b", "c", "d", "e", "f", "i", "s", "h", "r"]
    numbers = ['0', "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(numbers)
        nums += choice(numbers)

    person = {nums: {"name": name, "tel": tel}}
    return person


def write_json(person):
    try:
        data = json.load(open("persons.json"))
    except:
        FileNotFoundError
        data = []
    data.append(person)
    with open("persons.json", "w") as f:
        json.dump(data, f, indent=4)


for i in range(5):
    write_json(get_person())
