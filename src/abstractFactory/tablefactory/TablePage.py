from abstractFactory.factory.Page import Page

class TablePage(Page):
    def __init__(self, title, author):
        super(TablePage, self).__init__(title, author)

    def makeHTML(self):
        buffer = ""
        buffer += "<html><head><title>{0}</title></head>\n".format(self.title)
        buffer += "<body>\n"
        buffer += "<h1>{0}</h1>\n".format(self.title)
        buffer += "<table width=\"80%\" horder=\"3\">\n"
        for i in range(len(self.content)):
            buffer += "<tr>{0}</tr>".format(self.content[i].makeHTML())
        buffer += "</table>\n"
        buffer += "<hr><address>{0}</address>".format(self.author)
        buffer += "</body></html>\n"
        return buffer

