import importlib


class Factory(object):

    @staticmethod
    def get_factory(module_name, class_name):
        module = importlib.import_module(module_name)
        aclass = getattr(module, class_name)
        factory = aclass()
        return factory

    @classmethod
    def create_link(cls, caption, url):
        pass

    @classmethod
    def create_tray(cls, caption):
        pass

    @classmethod
    def create_page(cls, title, author):
        pass
