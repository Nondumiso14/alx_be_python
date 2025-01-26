class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a Book instance with title, author, and year.
        
        Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

