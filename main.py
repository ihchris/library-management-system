from models import Book, User, Library
from operations import lend_book
from utils import save_books, load_books

library = Library()
book = Book("1984", "George Orwell", "123")
user = User("Chris", 1)

library.books[book.ISBN] = book
library.users[user.ID] = user

lend_book(library, "123", user)

save_books(library.books, "data/books.json")
