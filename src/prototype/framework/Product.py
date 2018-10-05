from abc import ABCMeta, abstractclassmethod
import copy

class Product(metaclass=ABCMeta):

    @abstractclassmethod
    def use(self, s):
        pass

    @abstractclassmethod
    def create_clone(self):
        pass

    def clone(self, p):
        obj = copy.deepcopy(p)
        return obj