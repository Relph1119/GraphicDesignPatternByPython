from interpreter.Node import Node


class CommandNode(Node):
    def __init__(self):
        self.node = None

    def parse(self, context):
        from interpreter.RepeatCommandNode import RepeatCommandNode
        from interpreter.PrimitiveCommandNode import PrimitiveCommandNode
        if context.currentToken() == "repeat":
            self.node = RepeatCommandNode()
            self.node.parse(context)
        else:
            self.node = PrimitiveCommandNode()
            self.node.parse(context)

    def __str__(self):
        return self.node.__str__()
