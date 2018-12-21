from command.Command import Command


class MacroCommand(Command):
    def __init__(self):
        self.commands = list()

    def execute(self):
        for i in range(len(self.commands)):
            self.commands[i].execute()

    def append(self, cmd):
        if cmd != self:
            self.commands.append(cmd)

    def undo(self):
        if self.commands:
            self.commands.pop()

    def clear(self):
        self.commands.clear()
