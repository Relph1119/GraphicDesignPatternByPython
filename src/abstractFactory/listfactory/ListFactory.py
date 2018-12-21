from abstractFactory.factory.Factory import Factory
from abstractFactory.listfactory.ListComponent import ListLink, ListTray
from abstractFactory.listfactory.ListPage import ListPage


class ListFactory(Factory):
    def create_link(self, caption, url):
        return ListLink(caption, url)

    def create_tray(self, caption):
        return ListTray(caption)

    def create_page(self, title, author):
        return ListPage(title, author)
