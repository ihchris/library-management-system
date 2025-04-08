def lend_book(library, isbn, user):
    if isbn in library.books:
        book = library.books[isbn]
        if book.available:
            book.available = False
            user.borrowed_books.append(book)
            print(f"{user.name} borrowed '{book.title}'")
        else:
            print("Book not available")
    else:
        print("Book not found.")
