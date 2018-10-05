from abc import ABCMeta, abstractclassmethod

class Factory(metaclass=ABCMeta):
    
    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @abstractclassmethod
    def create_product(self, owner):
        pass

    @abstractclassmethod
    def register_product(self, product):
        pass