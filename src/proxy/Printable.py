from abc import ABCMeta, abstractstaticmethod

class Printable(metaclass=ABCMeta):
    @abstractstaticmethod
    def setPrinterName(self, name):
        pass

    @abstractstaticmethod
    def getPrinterName(self):
        pass

    @abstractstaticmethod
    def print(self,string):
        pass