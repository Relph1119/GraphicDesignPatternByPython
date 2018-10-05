from abc import ABCMeta, abstractclassmethod

class Print(metaclass=ABCMeta):
    @abstractclassmethod
    def print_weak(self):
        pass

    @abstractclassmethod
    def print_strong(self):
        pass
