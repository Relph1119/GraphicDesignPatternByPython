class Support(object):
    nextSupport = None

    def __init__(self, name):
        self.name = name

    def setNext(self, nextSupport):
        self.nextSupport = nextSupport
        return self.nextSupport

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif hasattr(self, "nextSupport") and self.nextSupport is not None:
            self.nextSupport.support(trouble)
        else:
            self.fail(trouble)

    @classmethod
    def resolve(cls, trouble):
        pass

    @classmethod
    def done(cls, trouble):
        print("{0} is resolved by [{1}]".format(trouble, cls.__name__))

    @classmethod
    def fail(cls, trouble):
        print("{0} cannot be resolved.".format(trouble))
