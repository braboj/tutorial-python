# Example: Serializing and Deserializing Objects with Pickle

import dill
import sys


class Book(object):

    def __init__(self, title, author, price, year):
        self.title = title
        self.author = author
        self.price = price
        self.year = year


if __name__ == "__main__":

    # Create junior book object
    book = Book(title='Python for Dummies', author='John Smith', price=25.0, year=2014)

    # Print the book object
    print(book.__dict__)

    # Serialize the book object
    serialized_book = dill.dumps(book)

    # Print the size of the serialized object
    print('Size of the serialized object: {} bytes'.format(sys.getsizeof(serialized_book)))

    # Print the serialized object
    print(serialized_book)

    # Deserialize the book object
    deserialized_book = dill.loads(serialized_book)

    # Print the book object
    print(deserialized_book.__dict__)
