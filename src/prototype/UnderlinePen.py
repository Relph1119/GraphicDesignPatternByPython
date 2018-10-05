from prototype.framework.Product import Product

class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s):
        length = len(s)
        print("\"{0}\"".format(s))
        print(" ", end='')
        for i in range(length):
            print(self.ulchar, end='')
        print("")

    def create_clone(self):
        return self.clone(self)

