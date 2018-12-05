from Builder import Builder

class HTMLBuilder(Builder):

    def makeTitle(self, title):
        self.filename = title
        self.file = open(title + '.html', 'w', encoding="utf8")
        self.file.write("<html><head><title>{0}</title></head><body>\n".format(title))
        self.file.write("<h1>{0}</h1>\n".format(title))

    def makeString(self, str):
        self.file.write("<p>{0}</p>\n".format(str))

    def makeItems(self, items):
        self.file.write("<ul>\n")
        for _, item in enumerate(items):
            self.file.write("<li>{0}</li>\n".format(item))
        self.file.write("</ul>\n")

    def close(self):
        self.file.write("</body></html>\n")
        self.file.close()

    def get_result(self):
        return self.filename