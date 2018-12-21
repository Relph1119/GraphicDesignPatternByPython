from BigChar import BigChar


class BigCharFactory:
    pool = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(BigCharFactory, cls).__new__(cls)
        return cls._instance

    def getBigChar(self, char_name):
        bc = self.pool.get(char_name)
        if not bc:
            bc = BigChar(char_name)
            self.pool.setdefault(char_name, bc)
        return bc
