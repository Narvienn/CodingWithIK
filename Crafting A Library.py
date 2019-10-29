"""Create a Library class for a library that will store books. A book can have a name, ISBN number and the author
- author should be defined in a separate class.

Extras:
1) do a while loop that will add a book to the library
2) display a list of books with their names and authors (in brackets)

EXTRA:
1. napisz metodę która usunie z biblioteki książkę o podanym indeksie
2. napisz metode która usunie z biblioteki książkę o podanej nazwie
3. napis metodę która zwróci książki z biblioteki o isbn większym niż nr podany w argumencie

zadanie ekstra:
spróbuj stworzyć formularz dodawania książek np. def get_book_from_user() który
- pobierze informacje potrzebne do stworzenia obiektu Book
- stworzy obiekt klasy Book z podanymi informacjami
- zwróci obiekt book

"""


class Library():
    books = None

    def __init__(self, name):
        self.books = []
        self.name = name

    def print_books(self, books):
        print(books)

    def add_books(self, book):
        self.books.append(book)

    def get_books(self):
        return self.books


class Author():
    author = ""

    def __init__(self, name):
        self.name = name


class Book():
    book = []

    def __init__(self, name, isbn):
        self.name = name
        self.isbn = isbn

    def add_author(self, author):
        self.book.append(author)


item1 = Book("Python for Dummies", "ISBN1234")
item2 = Book("Shakespeare's Collected Works", "ISBN2345")

local_library = Library("MSC Library")
local_library.books = [item1, item2]


""""
# 2) wyświetlanie listy książek - nim user zechce dodać ksiażkę, musi wiedzieć co już jest
    # wywołanie funkcji get_books, ino jak/na czym


# 1) pętla while, w której będzie się dodawać książkę

answer = input("Would you like to donate a book to the library? Y/N")
while answer == "Y":
    # inputy od usera + wywołanie funkcji add_books, ale na czym i jak przekazać toto do books"""



