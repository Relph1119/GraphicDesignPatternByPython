from abc import ABCMeta, abstractstaticmethod

class Mediator(metaclass=ABCMeta):
    @abstractstaticmethod
    def createColleagues(self):
        pass

    @abstractstaticmethod
    def colleagueChanged(self, event=None):
        pass
    