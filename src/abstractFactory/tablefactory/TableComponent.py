from abstractFactory.factory.Component import Link, Tray


class TableLink(Link):
    def __init__(self, caption, url):
        super(TableLink, self).__init__(caption, url)

    def makeHTML(self):
        return "<td><a href=\"{0}\">{1}</a></td>\n".format(self.url, self.caption)


class TableTray(Tray):
    def __init__(self, caption):
        super(TableTray, self).__init__(caption)

    def makeHTML(self):
        buffer = ""
        buffer += "<td>"
        buffer += "<table width=\"100%\" border=\"1\"><tr>"
        buffer += "<td bgcolor=\"#cccccc\" align=\"center\" colspan=\"{0}\"><b>{1}</b></td>".format(len(self.tray), self.caption)
        buffer += "<tr>\n"
        buffer += "<tr>\n"
        for _, tray in enumerate(self.tray):
            buffer += tray.makeHTML()
        buffer += "</tr></table>"
        buffer += "</td>"
        return buffer
