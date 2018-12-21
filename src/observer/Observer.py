class Observer(object):
    @classmethod
    def update(cls, generator):
        raise NotImplementedError
