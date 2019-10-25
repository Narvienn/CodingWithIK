"""Zadanie:
Stwórz zmienną "library" która będzie przechowywać książki w bibliotece. Książka
może mieć nazwę, isbn oraz autora, autora (osobna klasa) ustawiane w _init_
(Doczytasz ;-))

Dodatkowo spróbuj
1) napisać while'a w którym będzie można dodać kolejną książkę.
2) wyświetl listę książek z nazwą oraz listą autorów w nawiasie."""


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
    def __init__(self, name):
        self.name = name

class Book():
    def __init__(self, name, isbn):
        self.name = name
        self.isbn = isbn

    def add_author(self, name): # jw.



# stworzyć listę z obiektami typu Book
item1 = Book("Python for Dummies", "ISBN1234") # + autor
item2 = Book("Shakespeare's Collected Works", "ISBN2345")

local_library = Library()


""""
# 2) wyświetlanie listy książek - nim user zechce dodać ksiażkę, musi wiedzieć co już jest
    # wywołanie funkcji get_books, ino jak/na czym


# 1) pętla while, w której będzie się dodawać książkę

answer = input("Would you like to donate a book to the library? Y/N")
while answer == "Y":
    # inputy od usera vs wywołanie funkcji add_books, ale na czym i jak przekazać toto do book_roster -.-"""


