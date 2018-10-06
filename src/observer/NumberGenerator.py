from abc import ABCMeta, abstractstaticmethod

class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.observers = list()

    def addObserver(self, observer):
        self.observers.append(observer)

    def deleteObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for i in range(len(self.observers)):
            self.observers[i].update(self)

    @abstractstaticmethod
    def getNumber(self):
        pass

    @abstractstaticmethod
    def execute(self):
        pass