from abc import ABCMeta, abstractclassmethod

class Builder(metaclass=ABCMeta):
    @abstractclassmethod
    def makeTitle(self, title):
        pass

    @abstractclassmethod
    def makeString(self, str):
        pass

    @abstractclassmethod
    def makeItems(self, items):
        pass

    @abstractclassmethod
    def close(self):
        pass