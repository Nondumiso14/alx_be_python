class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
         return f"{self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (eBook, {self.file_size} MB)"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (Print Book, {self.page_count} pages)"

class Library:
    def __init__(self):

        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.

        Args:
        book (Book): The book to add to the library.
        """
        self.books.append(book)

   def list_books(self):
        """
        Prints details of each book in the library.
        """
        for book in self.books:
            print(book)
