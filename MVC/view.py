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
    @add_title(" Enter user data ")
    def wait_user_answer(self):
        # print(" Enter user data ".center(50, "="))
        print("Действия со статьями:")
        print("1 - add new title")
        print("2 - Show titles")
        print("3 - current title")
        print("4 - delete title")
        print("q Exit")
        user_answer = input("-> ")
        # print("=" * 50)
        return user_answer

    @add_title(" do title: ")
    def add_user_film(self):

        dict_article = {
            "title": None,
            "autor": None,
            "pages": None,
            "anons": None
        }
        # print(" do title: ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"enter new {key}: ")
        return dict_article

    @add_title(" list titles: ")
    def show_all_articles(self, articles):

        for ind, article in enumerate(articles, start=1):
            print(f"{ind}, {article}")

    @add_title(" Enter current title: ")
    def get_user_article(self):
        user_art = input("enter title: ")
        return user_art

    @add_title(" Show single title ")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} title - {article[key]}")

    @add_title(" Error ")
    def show_incurrect_error(self, article):
        print(f"No this title {article}")

    @add_title(" Removed ")
    def remove_single_article(self, article):
        print(f"Title {article} was removed")

    @add_title(" Error ")
    def show_incorrect_answer(self, answer):
        print(f"Uncorrected code {answer}")


