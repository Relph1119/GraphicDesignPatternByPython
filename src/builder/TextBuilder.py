from Builder import Builder

class TextBuilder(Builder):
    def __init__(self):
        self.buffer = str()

    def makeTitle(self, title):
        self.buffer += "==============================\n"
        self.buffer += " [ " + title +" ]\n"
        self.buffer += "\n"

    def makeString(self, str):
        self.buffer += '■ ' + str + "\n"
        self.buffer += "\n"

    def makeItems(self, items):
        for i in range(len(items)):
            self.buffer += "  · " + items[i] + "\n"
        self.buffer += "\n"

    def close(self):
        self.buffer += "==============================\n"

    def get_result(self):
        return self.buffer