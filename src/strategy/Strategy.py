from abc import ABCMeta, abstractstaticmethod

class Strategy(metaclass=ABCMeta):
    @abstractstaticmethod
    def nextHand(self):
        pass

    @abstractstaticmethod
    def study(self, win):
        pass
