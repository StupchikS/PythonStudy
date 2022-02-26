def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title} ".center(50, "="))
            output = func(*args, **kwargs)
            print(50 * "=")
            return output
        return wrap
    return wrapper


class UserInterface:
    @add_title(" Редактирование данных фильмотеки ")
    def wait_user_answer(self):
        # print(" Enter user data ".center(50, "="))
        print("Действия с фильмами: ")
        print("1 - добавить новый фильм")
        print("2 - показать фильмы")
        print("3 - поиск фильма")
        print("4 - удаление фильма")
        print("q Выход")
        user_answer = input("-> ")
        # print("=" * 50)
        return user_answer

    @add_title(" Добавление фильма: ")
    def add_user_film(self):
        dict_film = {
            "name": None,
            "genre": None,
            "director": None,
            "year": None,
            "duration": None,
            "atelier": None,
            "actors": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key}: ")
        return dict_film

    @add_title(" Ваша фильмотека: ")
    def show_all_films(self, films):

        for ind, film in enumerate(films, start=1):
            print(f"{ind}, {film}")

    @add_title(" Введите название фильма: ")
    def get_user_film(self):
        user_choose = input("Название фильма: ")
        return user_choose

    @add_title(" Просмотр выбранного фильма ")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} title - {film[key]}")

    @add_title(" Ошибка ")
    def show_uncurrect_error(self, film):
        print(f"У Вас нет такого фильма {film}")

    @add_title(" Удаление ")
    def remove_single_film(self, film):
        print(f"Фильм {film} был удален")

    @add_title(" Ошибка выбора меню ")
    def show_incorrect_answer(self, answer):
        print(f"Код в меню не обнаружен {answer}")


