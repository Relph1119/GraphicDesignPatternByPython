from abc import ABCMeta, abstractclassmethod

class Product(metaclass=ABCMeta):
    @abstractclassmethod
    def use(self):
        pass