from Iterator import Iterator

class BookShelfIterator(Iterator):
    def __init__(self, bookshelf):
        self.index = 0
        self.bookShelf = bookshelf

    def hasNext(self):
        if self.index < self.bookShelf.get_length():
            return True
        else:
            return False

    def next(self):
        book = self.bookShelf.get_book_at(self.index)
        self.index += 1
        return book
