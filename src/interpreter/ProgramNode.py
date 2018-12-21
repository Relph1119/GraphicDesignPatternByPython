from interpreter.Node import Node


class ProgramNode(Node):
    def __init__(self):
        self.commandListNode = None

    def parse(self, context):
        from interpreter.CommandListNode import CommandListNode
        context.skipToken("program")
        self.commandListNode = CommandListNode()
        self.commandListNode.parse(context)

    def __str__(self):
        return "[program {0}]".format(self.commandListNode)
