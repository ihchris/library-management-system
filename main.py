class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = True


class User:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.borrowed_books = []

    def __str__(self):
        return f"User: {self.name} (ID: {self.ID})"

    def __repr__(self):
        return f"<User('{self.name}', {self.ID})>"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
            self.books[book.ISBN] = book
    
    def lend_book(self, isbn, user):
        if isbn in self.books:
            book = self.books[isbn]
            if book.available:
                book.available = False
                user.borrowed_books.append(book)
                print(f"{user.name} borrowed '{book.title}'")
            else:
                print("Book not available")
        else:
            print("Book not found.")

# Creating library instance
library = Library()

# Creating book instance
book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "978-0-306-40615-7")

# Creating user instance
user1 = User("Christian", 1)

# Adding book to library
library.add_book(book1)

# User borrowing book
library.lend_book("978-0-306-40615-7", user1)

# Checking the status of the book and user
print("\n--- Current Status ---")
print(f"Book available? {book1.available}")
print(f"Books borrowed by {user1.name}: {[book.title for book in user1.borrowed_books]}")


