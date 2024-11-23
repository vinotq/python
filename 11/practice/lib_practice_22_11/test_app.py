import pytest
from app.main import Library, Book

lib = Library()

def test_empty_lib():
    assert "addBook" in dict(lib)
    assert "deleteBook" in dict(lib)
    assert "changeBookStatus" in dict(lib)
    assert "searchBookByTitle" in dict(lib)
    assert "searchBookByAuthor" in dict(lib)
    assert "searchBookByYear" in dict(lib)
    assert "saveLibrary" in dict(lib)
    assert "loadLibrary" in dict(lib)

def test_add_book():
    lib.addBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    assert lib.searchBookByTitle("The Great Gatsby")[0].dict() == {
        "id": 0,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "status": 0
    }

    lib.addBook("The Catcher in the Rye", "J.D. Salinger", 1951, 10)
    assert lib.searchBookByTitle("The Catcher in the Rye")[0].dict() == {
        "id": 10,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "year": 1951,
        "status": 0
    }

    lib.addBook("1984", "George Orwell", 1949, 11)
    assert lib.searchBookByTitle("1984")[0].dict() == {
        "id": 11,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "status": 0
    }

    lib.addBook("War and Peace", "Leo Tolstoy", 1869, status=1)
    assert lib.searchBookByTitle("War and Peace")[0].dict() == {
        "id": 1,
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "year": 1869,
        "status": 1
    }

def test_book_error():
    with pytest.raises(TypeError):
        Book(0, "The Great Gatsby", 1925)

    with pytest.raises(TypeError):
        Book(0, "The Great Gatsby", "F. Scott Fitzgerald", "1925")

    with pytest.raises(TypeError):
        Book(0, "The Great Gatsby", "F. Scott Fitzgerald", 1925, 10)

    with pytest.raises(TypeError):
        Book(0, "The Great Gatsby", "F. Scott Fitzgerald", 1925, status="10")
