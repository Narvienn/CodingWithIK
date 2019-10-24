"""Zadanie:
Stwórz zmienną "library" która będzie przechowywać książki w bibliotece. Książka
może mieć nazwę, isbn oraz autora, autora (osobna klasa) ustawiane w _init_
(Doczytasz ;-))

Dodatkowo spróbuj
1) napisać while'a w którym będzie można dodać kolejną książkę.
2) wyświetl listę książek z nazwą oraz listą autorów w nawiasie."""

class Library():
    book_roster = []
    def get_books(self):
        print(book_roster)

    def add_books(self):
        # funkcja na dodawanie nowych rekordów, którą potem wywoła się we while'u?
        # book_roster.append("user input??")

class Author():
    def __init__(self, author_name):
        self.author_name = author_name

class Book():
    def __init__(self, book_name, isbn):
        self.book_name = book_name
        self.isbn = isbn

    def get_author(self, author_name): # jw.
# gdzieś tu musi być autor, ale jak zrobić odwołanie do klasy Author()?

# stworzyć listę o nazwie library z obiektami typu Book
item1 = Book("Python for Dummies", "ISBN1234") # + autor!
item2 = Book("Shakespeare's Collected Works", "ISBN2345")

local_library = Library()
    # gdzie jak tu stworzyć listę z item1, item2 itd.?


# 2) wyświetlanie listy książek - nim user zechce dodać ksiażkę, musi wiedzieć co już jest
    # wywołanie funkcji get_books, ino jak/na czym


# 1) pętla while, w której będzie się dodawać książkę

answer = input("Would you like to donate a book to the library? Y/N")
while answer == "Y":
    # inputy od usera vs wywołanie funkcji add_books, ale na czym i jak przekazać toto do book_roster -.-


