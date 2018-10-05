from abc import ABCMeta, abstractstaticmethod
from visitor.FileTreatMentException import FileTreatMentException

class Entry(metaclass=ABCMeta):
    @abstractstaticmethod
    def getName(self):
        pass

    @abstractstaticmethod
    def getSize(self):
        pass

    @abstractstaticmethod
    def accept(self, visitor):
        pass

    def add(self, entry):
        raise FileTreatMentException

    def __str__(self):
        return "{0} ({1})".format(self.getName(), self.getSize())
