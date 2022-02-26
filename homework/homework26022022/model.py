import os.path
import pickle


class Filmoteka:
    def __init__(self, name, genre, director, year, duration, atelier, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.atelier = atelier
        self.actors = actors

    def __str__(self):
        return f"{self.name} ({self.genre} {self.year})"


class FilmotekaModel:
    def __init__(self):
        self.bd = "db.txt"
        self.films = self.load_data()

    def add_film(self, dict_film):
        film = Filmoteka(*dict_film.values())
        self.films[film.name] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_film):
        current = self.films[user_film]
        dict_film = {
            "name": current.name,
            "genre": current.genre,
            "director": current.director,
            "year": current.year,
            "duration": current.duration,
            "atelier": current.atelier,
            "actors": current.actors
        }
        return dict_film

    def remove_film(self, user_film):
        return self.films.pop(user_film)

    def save_data(self):
        with open(self.bd, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.bd):
            with open(self.bd, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
