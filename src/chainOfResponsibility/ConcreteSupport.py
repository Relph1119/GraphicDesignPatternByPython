from chainOfResponsibility.Support import Support

class NoSupport(Support):
    def resolve(self, trouble):
        return False

class LimitSupport(Support):
    def __init__(self, name, limit):
        super(LimitSupport, self).__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        return trouble.getNumber() < self.limit

class OddSupport(Support):
    def __init__(self, name):
        super(OddSupport, self).__init__(name)

    def resolve(self, trouble):
        return trouble.getNumber() % 2 == 1

class SpecialSupport(Support):
    def __init__(self, name, number):
        super(SpecialSupport, self).__init__(name)
        self.number = number

    def resolve(self, trouble):
        return trouble.getNumber() == self.number
