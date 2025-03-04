class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = True

    def check_out_book(self):
            pass
            
    def return_book(self):
        pass
    
class Library():
    def __init__(self):
        self._books = []
        self.checked_book = None

    def return_book(self, title):
        if title in self.checked_book:
            self._books.append(self.checked_book)

     def add_book(self, addbook):
        book = f"{addbook.title} by {addbook.author}"
        self._books.append(book)

    def check_out_book(self, title):
        if self._books == []:
            print("No books in the library.")
            return False

        for check in self._books:
            if title in check:
                self.checked_book = check
                self._books.remove(check)
                self.check_out_book = True
                return True
        print("No such book in the library.")
        return False
     def list_available_books(self):
        for book in self._books:
            print(book)

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
