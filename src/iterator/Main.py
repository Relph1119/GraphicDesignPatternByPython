from BookShelf import BookShelf
from Book import Book

if __name__ == '__main__':
    bookShelf = BookShelf(4)
    bookShelf.append_book(Book("Around the world in 80 Days"))
    bookShelf.append_book(Book("Bible"))
    bookShelf.append_book(Book("Cinderella"))
    bookShelf.append_book(Book("Daddy-Long-Legs"))
    it = bookShelf.iterator()
    while it.hasNext():
        book = it.next()
        print(book.name)

