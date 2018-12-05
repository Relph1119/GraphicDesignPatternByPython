class Manager:
    def __init__(self):
        self.showcase = dict()

    def register(self, name, proto):
        self.showcase[name] = proto

    def create(self, proto_name):
        p = self.showcase.get(proto_name)
        return p.create_clone()