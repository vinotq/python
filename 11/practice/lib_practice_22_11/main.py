from main import Library

if __name__ == "__main__":
    library = Library()
    library.addBook("The Great Gatsby", "F Scott Fitzgerald", 1925)
    library.addBook("The Catcher in the Rye", "J.D. Salinger", 1951)
    library.addBook("1984", "George Orwell", 1949)
    print(library)
    print("---------------------")
    library.changeBookStatus(0, 1)
    print(library)
