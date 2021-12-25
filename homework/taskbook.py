class BookClass:
    title_book = ""
    year_book = ""
    publish_book = ""
    type_book = ""
    author_book = ""
    price_book = ""

    def print_book_class(self):
        print(" Information about book".center(40, "*"))
        print(
            f"Название книги: {self.title_book}\nГод издания: {self.year_book}\nИздательство: {self.publish_book}\n"
            f"Жанр: {self.type_book}\nАвтор книги: {self.author_book}\nЦена: {self.price_book}")
        print("=" * 40)

    def info_book_class(self, title, year, publish, typeb, author, price):
        self.title_book = title
        self.year_book = year
        self.publish_book = publish
        self.type_book = typeb
        self.author_book = author
        self.price_book = price

    def set_title(self, title):
        self.title_book = title

    def set_year(self, year):
        self.year_book = year

    def set_publish(self, publish):
        self.publish_book = publish

    def set_type(self, typeb):
        self.type_book = typeb

    def set_author(self, author):
        self.author_book = author

    def set_price(self, price):
        self.price_book = price

    def get_title(self):
        return self.title_book

    def get_year(self):
        return self.year_book

    def get_publish(self):
        return self.publish_book

    def get_type(self):
        return self.type_book

    def get_author(self):
        return self.author_book

    def get_price(self):
        return self.price_book


book1 = BookClass()
book1.print_book_class()
book1.info_book_class("Незнайка на луне", "1995", "Детская литература", "Детская литература", "Николай Носов", "450")
book1.print_book_class()
book2 = BookClass()
book2.set_year("2015")
book2.set_price("123")
book2.set_title("Путь")
book2.set_publish("Москва Возвращение")
book2.set_type("Мемуары")
book2.set_author("Ольга Адамова-Слизберг")
book2.print_book_class()
print(book2.get_title())
print(book1.get_title())
