from BigChar import BigChar

class BigCharFactory():
    pool = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(BigCharFactory, cls).__new__(cls)
        return cls._instance

    def getBigChar(self, charname):
        bc = self.pool.get(charname)
        if bc is None:
            bc = BigChar(charname)
            self.pool.setdefault(charname, bc)
        return bc