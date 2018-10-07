from abc import ABCMeta, abstractstaticmethod

class State(metaclass=ABCMeta):
    @abstractstaticmethod
    def doClouck(self, context, hour):
        pass

    @abstractstaticmethod
    def doUse(self, context):
        pass

    @abstractstaticmethod
    def doAlarm(self, context):
        pass

    @abstractstaticmethod
    def doPhone(self, context):
        pass