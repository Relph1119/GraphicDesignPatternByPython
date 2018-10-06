from interpreter.Node import Node


class RepeatCommandNode(Node):
    def __init__(self):
        self.number = 0
        self.commandListNode = None

    def parse(self, context):
        from interpreter.CommandListNode import CommandListNode
        context.skipToken("repeat")
        self.number = context.currentToken()
        context.nextToken()
        self.commandListNode = CommandListNode()
        self.commandListNode.parse(context)

    def __str__(self):
        return "[repeat {0} {1}]".format(self.number, self.commandListNode)
