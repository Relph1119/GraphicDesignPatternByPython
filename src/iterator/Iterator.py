class Iterator(object):
    @classmethod
    def hasNext(cls):
        raise NotImplementedError

    @classmethod
    def next(cls):
        raise NotImplementedError
