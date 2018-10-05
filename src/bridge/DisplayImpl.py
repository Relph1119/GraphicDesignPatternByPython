from abc import ABCMeta, abstractclassmethod

class DisplayImpl(metaclass=ABCMeta):
    @abstractclassmethod
    def rawOpen(self):
        pass

    @abstractclassmethod
    def rawPrint(self):
        pass

    @abstractclassmethod
    def rawClose(self):
        pass
