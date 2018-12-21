class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.makeTitle("Greeting")
        self.builder.makeString("从早上至下午")
        self.builder.makeItems(["早上好。", "下午好。"])
        self.builder.makeString("晚上")
        self.builder.makeItems(["晚上好。", "晚安。", "再见。"])
        self.builder.close()
