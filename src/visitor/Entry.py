from visitor.FileTreatMentException import FileTreatMentException


class Entry(object):
    @classmethod
    def getName(cls):
        raise NotImplementedError

    @classmethod
    def getSize(cls):
        raise NotImplementedError

    @classmethod
    def accept(cls, visitor):
        raise NotImplementedError

    def add(self, entry):
        raise FileTreatMentException

    def __str__(self):
        return "{0} ({1})".format(self.getName(), self.getSize())
