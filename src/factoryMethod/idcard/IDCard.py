from framework.Product import Product


class IDCard(Product):
    def __init__(self, owner):
        print("制作{0}的ID卡。".format(owner))
        self.owner = owner

    def use(self):
        print("使用{0}的ID卡。".format(self.owner))
