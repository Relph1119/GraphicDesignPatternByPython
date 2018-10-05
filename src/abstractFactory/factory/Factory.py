from abc import ABCMeta, abstractclassmethod
import importlib

class Factory(metaclass=ABCMeta):

    @staticmethod
    def get_factory(module_name, class_name):
        module = importlib.import_module(module_name)
        aclass = getattr(module, class_name)
        factory = aclass()
        return factory

    @abstractclassmethod
    def create_link(self, caption, url):
        pass

    @abstractclassmethod
    def create_tray(self, caption):
        pass

    @abstractclassmethod
    def create_page(self, title, author):
        pass


