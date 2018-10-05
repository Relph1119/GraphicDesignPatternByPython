from abc import ABCMeta, abstractstaticmethod

class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def setNext(self, nextSupport):
        self.nextSupport = nextSupport
        return self.nextSupport

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif hasattr(self, "nextSupport") and not self.nextSupport is None:
            self.nextSupport.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return "[{0}]".format(self.name)

    @abstractstaticmethod
    def resolve(self, trouble):
        pass

    def done(self, trouble):
        print("{0} is resolved by {1}".format(trouble, self))

    def fail(self, trouble):
        print("{0} cannot be resolved.".format(trouble))