class Banner:
    def __init__(self, name):
        self.name = name

    def show_with_paren(self):
        print("({0})".format(self.name))

    def show_with_aster(self):
        print("*{0}*".format(self.name))
