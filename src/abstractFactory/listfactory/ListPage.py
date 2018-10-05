from abstractFactory.factory.Page import Page

class ListPage(Page):
    def __init__(self, title, author):
        super(ListPage, self).__init__(title, author)

    def makeHTML(self):
        buffer = ""
        buffer += "<html><head><title>{0}</title></head>\n".format(self.title)
        buffer += "<body>\n"
        buffer += "<h1>{0}</h1>\n".format(self.title)
        buffer += "<ul>\n"
        for i in range(len(self.content)):
            buffer += self.content[i].makeHTML()
        buffer += "</ul>\n"
        buffer += "<hr><address>{0}</address>".format(self.author)
        buffer += "</body></html>\n"
        return buffer