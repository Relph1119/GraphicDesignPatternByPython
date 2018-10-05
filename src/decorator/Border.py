from abc import ABCMeta, abstractstaticmethod

class Border(metaclass=ABCMeta):
    def __init__(self, display):
        self.display = display