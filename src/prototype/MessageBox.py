from prototype.framework.Product import Product

class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s):
        length = len(s)
        for i in range(length + 4):
            print(self.decochar, end='')
        print("")
        print("{0} {1} {2}".format(self.decochar, s, self.decochar))
        for i in range(length + 4):
            print(self.decochar, end='')
        print("")

    def create_clone(self):
        return self.clone(self)

