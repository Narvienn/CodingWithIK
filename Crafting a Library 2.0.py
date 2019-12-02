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

# write a method that will remove a book from the library by its name
    def remove_book_by_name(self, name):
        for book in self.books:
            if book.name == name:
                idx = self.books.index(book)
                self.remove_book_by_name(idx)  # TODO: HOW TO run this method on an object in console?

# write a method that will remove a book from the library by its index
    def remove_book_by_index(self, index):
        del self.books[index]

# write a method that will return any books with ISBN number greater than provided in the argument
    def get_book_by_isbn_above_number(self):
        for book in self.books:
            isbn_number = int(book.isbn.strip("ISBN"))
            if isbn_number > 1234:
                return book


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
        return author

    def get_books_from_user(self, book):
        self.name = input(print("What's the book's name?"))
        print(self.name)
        self.book.append(self.name)
        self.isbn = input("OK. What's the ISBN number of the book?")
        self.book.append(self.isbn)
        author = input("And who is the author?")
        self.book.append(author)
        return book
