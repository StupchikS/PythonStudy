import os.path
import pickle


class Article:
    def __init__(self, title, author, pages, anons):
        self.title = title
        self.author = author
        self.pages = pages
        self.anons = anons

    def __str__(self):
        return f"{self.title} ({self.author})"


class ArticleModel:
    def __init__(self):
        self.bd = "db.txt"
        self.articles = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        current = self.articles[user_title]
        dict_article = {
            "title": current.title,
            "author": current.author,
            "pages": current.pages,
            "anons": current.anons
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def save_data(self):
        with open(self.bd, "wb") as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        if os.path.exists(self.bd):
            with open(self.bd, "rb") as f:
                return pickle.load(f)
        else:
            return dict()
