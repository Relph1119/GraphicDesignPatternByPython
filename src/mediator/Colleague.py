from abc import ABCMeta, abstractstaticmethod

class Colleague(metaclass=ABCMeta):
    @abstractstaticmethod
    def setMediator(self, mediator):
        pass

    @abstractstaticmethod
    def setColleagueEnable(self, enable):
        pass
