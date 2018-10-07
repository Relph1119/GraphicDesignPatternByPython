from abc import ABCMeta, abstractstaticmethod

class Drawable(metaclass=ABCMeta):
    @abstractstaticmethod
    def draw(self):
        pass