from abc import ABCMeta, abstractclassmethod

class Iterator(metaclass=ABCMeta):
    @abstractclassmethod
    def hasNext(self):
        pass

    @abstractclassmethod
    def next(self):
        pass
