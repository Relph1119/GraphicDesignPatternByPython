from FileTreatMentException import FileTreatMentException


class Entry(object):
    @classmethod
    def getName(cls):
        raise NotImplementedError

    @classmethod
    def getSize(cls):
        raise NotImplementedError

    def add(self, entry):
        raise FileTreatMentException

    @classmethod
    def printList(cls, prefix=""):
        raise NotImplementedError

    def __str__(self):
        return "{0} ({1})".format(self.getName(), self.getSize())