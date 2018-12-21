class DisplayImpl(object):
    @classmethod
    def rawOpen(cls):
        raise NotImplementedError

    @classmethod
    def rawPrint(cls):
        raise NotImplementedError

    @classmethod
    def rawClose(cls):
        raise NotImplementedError
