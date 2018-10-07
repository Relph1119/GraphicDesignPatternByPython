from abc import ABCMeta, abstractstaticmethod

class Command(metaclass=ABCMeta):
    @abstractstaticmethod
    def execute(self):
        pass