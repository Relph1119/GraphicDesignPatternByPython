from abc import ABCMeta, abstractstaticmethod

class Visitor(metaclass=ABCMeta):
    @abstractstaticmethod
    def visit(self, entry):
        pass