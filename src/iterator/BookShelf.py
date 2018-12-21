from Aggregate import Aggregate
from Book import Book
from BookShelfIterator import BookShelfIterator


class BookShelf(Aggregate):

    last = 0

    def __init__(self, maxsize):
        self.books = [object for m in range(maxsize)]

    def get_book_at(self, index):
        return self.books[index]

    def append_book(self, book=Book):
        self.books[self.last] = book
        self.last += 1

    def get_length(self):
        return self.last

    def iterator(self):
        return BookShelfIterator(self)
