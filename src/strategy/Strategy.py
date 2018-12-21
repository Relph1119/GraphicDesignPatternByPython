class Strategy(object):
    @classmethod
    def nextHand(cls):
        raise NotImplementedError

    @classmethod
    def study(cls, win):
        raise NotImplementedError
