from framework.Factory import Factory
from idcard.IDCard import IDCard

class IDCardFactory(Factory):
    def __init__(self):
        self.owners = set()

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.owners.add(product.owner)
    