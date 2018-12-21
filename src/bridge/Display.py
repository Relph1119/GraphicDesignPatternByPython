class Display:
    def __init__(self, impl):
        self.impl = impl

    def open(self):
        self.impl.rawOpen()

    def print(self):
        self.impl.rawPrint()

    def close(self):
        self.impl.rawClose()

    def display(self):
        self.open()
        self.print()
        self.close()
