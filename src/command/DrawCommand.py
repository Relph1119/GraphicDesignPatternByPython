from command.Command import Command

class DrawCommand(Command):
    def __init__(self, master, event, color="red"):
        self.x = event.x
        self.y = event.y
        self.master = master
        self.color = color

    def execute(self):
        x1, y1 = (self.x - 6), (self.y - 6)
        x2, y2 = (self.x + 6), (self.y + 6)
        self.master.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

