class AbstractDisplay(object):
    @classmethod
    def open(cls):
        raise NotImplementedError

    @classmethod
    def print(cls):
        raise NotImplementedError

    @classmethod
    def close(cls):
        raise NotImplementedError

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()
