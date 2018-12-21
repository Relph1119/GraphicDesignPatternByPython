from abstractFactory.factory.Page import Page


class ListPage(Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def makeHTML(self):
        buffer = ""
        buffer += "<html><head><title>{0}</title></head>\n".format(self.title)
        buffer += "<body>\n"
        buffer += "<h1>{0}</h1>\n".format(self.title)
        buffer += "<ul>\n"
        for _, content in enumerate(self.content):
            buffer += content.makeHTML()
        buffer += "</ul>\n"
        buffer += "<hr><address>{0}</address>".format(self.author)
        buffer += "</body></html>\n"
        return buffer
