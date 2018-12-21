class Factory(object):
    
    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(p)
        return p

    @classmethod
    def create_product(cls, owner):
        raise NotImplementedError

    @classmethod
    def register_product(cls, product):
        raise NotImplementedError
