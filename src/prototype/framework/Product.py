import copy


class Product(object):

    @classmethod
    def use(cls, s):
        raise NotImplementedError

    @classmethod
    def create_clone(cls):
        raise NotImplementedError

    def clone(self, p):
        obj = copy.deepcopy(p)
        return obj
