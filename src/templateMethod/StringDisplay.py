from AbstractDisplay import AbstractDisplay


class StringDisplay(AbstractDisplay):
    def __init__(self, name):
        self.name = name
        self.width = len(name)

    def open(self):
        self.print_line()

    def print(self):
        print("|{0}|".format(self.name))

    def close(self):
        self.print_line()

    def print_line(self):
        print("+", end='')
        for i in range(self.width):
            print("-", end='')
        print("+")
