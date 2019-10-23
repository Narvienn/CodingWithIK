"""Zadanie:
Stwórz zmienną "library" która będzie przechowywać książki w bibliotece. Książka
może mieć nazwę, isbn oraz autora, autora (osobna klasa) ustawiane w _init_
(Doczytasz ;-))

Dodatkowo spróbuj
1) napisać while'a w którym będzie można dodać kolejną książkę.
2) wyświetl listę książek z nazwą oraz listą autorów w nawiasie."""

class Library():
    def get_books(self):
        print(" #obiekt z klasy Library, ale jak go tutaj zdefiniować")

class Author():
    def __init__(self, author_name):
        self.author_name = author_name

class Book():
    def __init__(self, book_name, isbn):
        self.book_name = book_name
        self.isbn = isbn

    def get_author(self, author_name): # jw.
# gdzieś tu musi być autor, ale jak zrobić odwołanie do klasy Author()?


# 2) wyświetlanie listy książek - nim user zechce dodać ksiażkę, musi wiedzieć co już jest

print("Display the list of available books.")


# 1) pętla while, w której będzie się dodawać książkę

answer = input("Would you like to donate a book? Y/N")
while answer == "Y":
    # inputy od usera: book name, author, isbn
    #

# stworzyć listę o nazwie library z obiektami typu Book
    """"
    book1 = {
        "book_name": "Python for Dummies",
        "author": "Stef Maruch",
        "isbn": "ISBN0123"
    }

    book2 = {
        "book_name": "nazwa_ksiazki2",
        "author": "Some Writer2",
        "isbn": "ISBN1234"""
    }