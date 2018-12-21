class NumberGenerator(object):
    def __init__(self):
        self.observers = list()

    def addObserver(self, observer):
        self.observers.append(observer)

    def deleteObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for _, observer in enumerate(self.observers):
            observer.update(self)

    @classmethod
    def getNumber(cls):
        raise NotImplementedError

    @classmethod
    def execute(cls):
        raise NotImplementedError
