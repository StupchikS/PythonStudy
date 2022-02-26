from view import UserInterface
from model import FilmotekaModel


class Controller:
    def __init__(self):
        self.film_model = FilmotekaModel()
        self.user_interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film = self.user_interface.add_user_film()
            self.film_model.add_film(film)
        elif answer == "2":
            films = self.film_model.get_all_films()
            self.user_interface.show_all_films(films)
        elif answer == "3":
            film_name = self.user_interface.get_user_film()
            try:
                film = self.film_model.get_single_film(film_name)
            except KeyError:
                self.user_interface.show_uncurrect_error(film_name)
            else:
                self.user_interface.show_single_film(film)
        elif answer == "4":
            film_name = self.user_interface.get_user_film()
            try:
                name = self.film_model.remove_film(film_name)
            except KeyError:
                self.user_interface.show_incorrect_answer(film_name)
            else:
                self.user_interface.remove_single_film(name)
        elif answer == "q":
            self.film_model.save_data()
        else:
            self.user_interface.show_incorrect_answer(answer)




