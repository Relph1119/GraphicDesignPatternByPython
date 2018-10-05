from chainOfResponsibility.Support import Support

class NoSupport(Support):
    def __init__(self, name):
        self.name = name

    def resolve(self, trouble):
        return False

class LimitSupport(Support):
    def __init__(self, name, limit):
        super(LimitSupport, self).__init__(name)
        self.limit = limit

    def resolve(self, trouble):
        if trouble.getNumber() < self.limit:
            return True
        else:
            return False

class OddSupport(Support):
    def __init__(self, name):
        super(OddSupport, self).__init__(name)

    def resolve(self, trouble):
        if trouble.getNumber() % 2 == 1:
            return True
        else:
            return False


class SpecialSupport(Support):
    def __init__(self, name, number):
        super(SpecialSupport, self).__init__(name)
        self.number = number

    def resolve(self, trouble):
        if trouble.getNumber() == self.number:
            return True
        else:
            return False
