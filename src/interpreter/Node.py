from abc import ABCMeta, abstractstaticmethod

class Node(metaclass=ABCMeta):
    @abstractstaticmethod
    def parse(self, context):
        pass