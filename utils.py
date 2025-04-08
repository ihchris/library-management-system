import json

def save_books(books, filename):
    with open(filename, "w") as f:
        json.dump({isbn: vars(book) for isbn, book in books.items()}, f)

def load_books(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        from models import Book
        return {isbn: Book(**info) for isbn, info in data.items()}
