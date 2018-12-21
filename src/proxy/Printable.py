class Printable(object):
    @classmethod
    def setPrinterName(cls, name):
        raise NotImplementedError

    @classmethod
    def getPrinterName(cls):
        raise NotImplementedError

    @classmethod
    def print(cls, string):
        raise NotImplementedError
