from abc import ABCMeta, abstractstaticmethod

class Context(metaclass=ABCMeta):
    @abstractstaticmethod
    def setClock(self, hour):
        pass

    @abstractstaticmethod
    def changeState(self, state):
        pass

    @abstractstaticmethod
    def callSecurityCenter(self, msg):
        pass

    @abstractstaticmethod
    def recordLog(self, msg):
        pass