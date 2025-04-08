class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({self.ISBN})"


class User:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name} (ID: {self.ID})"


class Library:
    def __init__(self):
        self.books = {}  # isbn: Book
        self.users = {}  # id: User
