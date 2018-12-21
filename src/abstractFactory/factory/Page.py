class Page(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = list()

    def add(self, item):
        self.content.append(item)

    def output(self):
        filename = self.title + ".html"
        file = open(filename, "w", encoding="gbk")
        file.write(self.makeHTML())
        file.close()
        print("{0}编写完成。".format(filename))

    @classmethod
    def makeHTML(cls):
        pass
