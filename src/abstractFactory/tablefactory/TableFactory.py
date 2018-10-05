from abstractFactory.factory.Factory import Factory
from abstractFactory.tablefactory.TableComponent import TableLink, TableTray
from abstractFactory.tablefactory.TablePage import TablePage

class TableFactory(Factory):
    def create_link(self, caption, url):
        return TableLink(caption, url)

    def create_tray(self, caption):
        return TableTray(caption)

    def create_page(self, title, author):
        return TablePage(title, author)