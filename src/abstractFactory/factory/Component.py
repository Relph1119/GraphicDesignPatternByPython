class Item(object):
    def __init__(self, caption):
        self.caption = caption

    @classmethod
    def makeHTML(cls):
        raise NotImplementedError


class Link(Item):
    def __init__(self, caption, url):
        super().__init__(caption)
        self.url = url


class Tray(Item):
    def __init__(self, caption):
        super().__init__(caption)
        self.tray = list()

    def add(self, item):
        self.tray.append(item)
