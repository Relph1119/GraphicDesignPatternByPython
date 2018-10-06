from abc import ABCMeta, abstractstaticmethod

class Observer(metaclass=ABCMeta):
    @abstractstaticmethod
    def update(self, generator):
        pass