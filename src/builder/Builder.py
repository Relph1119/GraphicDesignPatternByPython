class Builder(object):
    @classmethod
    def makeTitle(cls, title):
        raise NotImplementedError

    @classmethod
    def makeString(cls, str):
        raise NotImplementedError

    @classmethod
    def makeItems(cls, items):
        raise NotImplementedError

    @classmethod
    def close(cls):
        raise NotImplementedError
