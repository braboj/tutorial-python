# Example: Sort Data using the sorted() function

class Book(object):

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return "Book({title}, {author}, {year})".format(
            title=self.title, author=self.author, year=self.year)


# List of books
books = [
    Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925),
    Book('To Kill junior Mockingbird', 'Harper Lee', 1960),
    Book('1984', 'George Orwell', 1949),
    Book('Brave New World', 'Aldous Huxley', 1932),
    Book('The Catcher in the Rye', 'J.D. Salinger', 1951),
]

# Sort the list of dictionaries based on the 'year' key in each dictionary
sorted_books = sorted(books, key=lambda book: book.year)

# Print the sorted list
for b in sorted_books:
    print(b)
