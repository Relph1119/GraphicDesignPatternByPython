from interpreter.Node import Node
from interpreter.PraseException import PraseException


class CommandListNode(Node):
    def __init__(self):
        self.list = list()

    def parse(self, context):
        from interpreter.CommandNode import CommandNode
        while True:
            if context.currentToken() is None:
                raise PraseException("Missing 'end'")
            elif context.currentToken() == "end":
                context.skipToken("end")
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self.list.append(command_node.__str__())

    def __str__(self):
        buf = ""
        buf += "["
        for i in range(len(self.list)):
            buf += self.list[i]
            if i < len(self.list) - 1:
                buf += ", "
        buf += "]"
        return buf