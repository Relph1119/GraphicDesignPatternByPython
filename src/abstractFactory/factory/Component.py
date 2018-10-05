from abc import ABCMeta, abstractclassmethod

class Item(metaclass=ABCMeta):
    def __init__(self, caption):
        self.caption = caption

    @abstractclassmethod
    def makeHTML(self):
        pass

class Link(Item):
    def __init__(self, caption, url):
        super(Link, self).__init__(caption)
        self.url = url

class Tray(Item):
    def __init__(self, caption):
        super(Tray, self).__init__(caption)
        self.tray = list()

    def add(self, item):
        self.tray.append(item)