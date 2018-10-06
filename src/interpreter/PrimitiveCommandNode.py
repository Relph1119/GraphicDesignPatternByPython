from interpreter.Node import Node
from interpreter.PraseException import PraseException

class PrimitiveCommandNode(Node):
    def __init__(self):
        self.name = ""

    def parse(self, context):
        self.name = context.currentToken()
        context.skipToken(self.name)
        if self.name != "go" and self.name != "right" and self.name != "left":
            raise PraseException(self.name + " is undefined")

    def __str__(self):
        return self.name