from abc import ABCMeta, abstractclassmethod

class Aggregate(metaclass=ABCMeta):
    @abstractclassmethod
    def iterator(self):
        pass
