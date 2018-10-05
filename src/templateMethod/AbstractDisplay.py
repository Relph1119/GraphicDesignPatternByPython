from abc import ABCMeta, abstractclassmethod

class AbstractDisplay(metaclass=ABCMeta):
    @abstractclassmethod
    def open(self):
        pass

    @abstractclassmethod
    def print(self):
        pass

    @abstractclassmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()