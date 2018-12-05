from Printable import Printable
from Printer import Printer

class PrinterProxy(Printable):

    def __init__(self, name):
        self.name = name
        self.real = None

    def setPrinterName(self, name):
        if self.real:
            self.real.setPrinterName(name)
        self.name = name

    def getPrinterName(self):
        return self.name

    def print(self, string):
        self.realize()
        self.real.print(string)

    def realize(self):
        if not self.real:
            self.real = Printer(self.name)
