class Visitor(object):
    @classmethod
    def visit(cls, entry):
        raise NotImplementedError
