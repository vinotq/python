from __future__ import annotations
from enum import Enum
from typing import Any

class Status(Enum):
    IN_STOCK = 0
    ISSUED = 1

class Book:
    def __init__(self, id: int, title: str, author: str, year: int):
        if not isinstance(title, str):
            raise TypeError(f"Title must be a string, but got {type(title)}")

        if not isinstance(author, str):
            raise TypeError(f"Author must be a string, but got {type(author)}")

        if not isinstance(year, int):
            raise TypeError(f"Year must be an integer, but got {type(year)}")

        if not isinstance(id, int):
            raise TypeError(f"Id must be an integer, but got {type(id)}")

        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = Status.IN_STOCK

    def __str__(self):
        return f"{self.id} {self.title} {self.author} {self.year} {self.status}"


class Library:
    def __init__(self):
        self.__books = {}
        self.__id_increment = 0

    def addBook(self, title: str, author: str, year: int):
        try:
            book = Book(self.__id_increment, title, author, year)
            self.__books[self.__id_increment] = book
            self.__id_increment += 1
        except Exception as e:
            print(f"Exception: {e}\nBook was not added")

    def deleteBook(self, id: int):
        if not isinstance(id, int):
            raise TypeError(f"Id must be an integer, but got {type(id)}")

        if id not in self.__books:
            raise KeyError(f"Book with id {id} not found")

        del self.__books[id]

    def searchBookByTitle(self, title: str):
        return [
            book for book in self.__books.values() if title.lower() in book.title.lower()
        ]

    def searchBookByAuthor(self, author: str):
        return [
            book for book in self.__books.values() if author.lower() in book.author.lower()
        ]

    def searchBookByYear(self, year: int):
        return [book for book in self.__books.values() if book.year == year]

    def __str__(self):
        return "\n".join(map(str, self.__books.values()))

    def changeBookStatus(self, id: int, status: Status):
        if not isinstance(id, int):
            raise TypeError(f"Id must be an integer, but got {type(id)}")

        if id not in self.__books:
            raise KeyError(f"Book with id {id} not found")

        if isinstance(status, int):
            status = Status(status)

        self.__books[id].status = status


if __name__ == "__main__":
    library = Library()
    library.addBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    library.addBook("The Catcher in the Rye", "J.D. Salinger", 1951)
    library.addBook("1984", "George Orwell", 1949)
    print(library)
    print("---------------------")
    library.changeBookStatus(0, 1)
    print(library)
    print("---------------------")
    library.changeBookStatus(0, Status.IN_STOCK)
    print(library)


