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

    # EXTRA/while loop:
    def get_book_from_user(self, books):
        new_book = Book()

        # 1. create a Book object ( = a list),
        # 2. get name, isbn and author from the user,
        # 3. append those to the book object
        # 4. add the new_book to library

    # extra 1: define a method for removing a book from library by its index
    def remove_book_by_index(self, index):
        del self.books[index]

    # extra 2: define a method for removing a book by its name
    def remove_book_by_name(self, name):
        # book = Book(jakies_argumenty)
        # self.books = [book, Book(kolejen_argumenty, "ksiazka stringiem"]
        for book in self.books:
            if book.name == name:
                idx = self.books.index(book)

                self.remove_book_by_index(idx)

        # idx = self.books.index("ksiazka stringiem")

    # extra 3: define a method for returning a book with ISBN larger than provided in the argument
    # Q: how/why do I include the specific int in the argument?
    def get_book_by_isbn_above_number(self, isbn_number):
        for book in self.books:
            isbn_comparison = int(book.isbn.strip("ISBN"))
            # isbn is an alphanumeric string - 1. remove the leading "ISBN" part, 2. convert str to int for comparison
            if int(book.isbn.strip("ISBN")) > isbn_number
                return book


class Author():

    def __init__(self, name):
        self.name = name


class Book():

    def __repr__(self):
        return "Reprezentacja: {} {}".format(self.name, self.isbn)


def __init__(self, name, isbn):
    self.name = name
    self.isbn = isbn


def add_author(self, author):  ####### ta zmienna jest przekazana tuuuuu
    self.book.append(author)  ####a tu przekazana po raz 2
    return author


### Czyli na poczatku piszemy to co nizej >>>>

author2 = Author("Ursula K. Le Guin")

item1 = Book("Python for Dummies", "ISBN1234")
wartosc_zwracana = item1.add_author(author1)

author1 = Author("Stef Maruch").  #### definicja zmiennej
author = Book("Python for Dummies", "ISBN1234", ).add_author(author1)  ### przekazanie tej zmiennej po raz 1.

item2 = Book("The Telling", "ISBN2345").add_author(author2)
item3 = Book("Left Hand of Darkness", "ISBN3456").add_author(author2)

local_library = Library("MSC Library")
local_library.add_books(item1)
local_library.add_books(item2)
local_library.add_books(item3)

print(local_library.get_books())

for book in local_library.get_books():
    print(book)
    ## Wysiwelit: Reprezentacja: Python for Dummies ISBN1234

local_library.print_books()

# Wyswietli: ['Python for Dummies', 'bbb']

local_library.remove_book_by_name("ktos")

"""




Python 2.7.16 (default, Oct 17 2019, 17:14:30)
[GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.32.4) (-macos10.15-objc-s on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> class Book():
...    pass
...
>>>
>>>
>>> print([Book(), Book()])
[<__main__.Book instance at 0x1051d9878>, <__main__.Book instance at 0x1051d98c0>]


"""

# badz
author_name = "some name"
local_library.remove_book_by_name(author_name)


# 2) displaying books in library
for book in local_library:
    del book[1] # 0 - name, 1 - isbn, 2 - author
    print(local_library) # jak wrzucić autora w nawias...?

# 1) add a while loop in which user will have the option of adding books

answer = input("Would you like to donate a book to the library? Y/N")
while answer == "Y":
    book_name = input("Please provide the name of your book.")
    local_library.add_book(book_name)
    isbn_name = input("Great. Now please provide the ISBN number.")

