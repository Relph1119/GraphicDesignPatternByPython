from abc import ABCMeta, abstractstaticmethod
from FileTreatMentException import FileTreatMentException

class Entry(metaclass=ABCMeta):
    @abstractstaticmethod
    def getName(self):
        pass

    @abstractstaticmethod
    def getSize(self):
        pass

    def add(self, entry):
        raise FileTreatMentException

    @abstractstaticmethod
    def printList(self, prefix=""):
        pass

    def __str__(self):
        return "{0} ({1})".format(self.getName(), self.getSize())