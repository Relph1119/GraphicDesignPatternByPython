import tkinter
from command.DrawCommand import DrawCommand
from command.MacroCommand import MacroCommand

class CanvasFrame(tkinter.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        self.history = MacroCommand()
        self.paintColor = "red"

        self.clearButton = tkinter.Button(self, text="clear")
        self.undoButton = tkinter.Button(self, text="undo")
        self.redButton = tkinter.Button(self, text="red")
        self.greenButton = tkinter.Button(self, text="green")
        self.blueButton = tkinter.Button(self, text="blue")
        self.canvas = tkinter.Canvas(self, width=400, height=300, bg="white")

        self.redButton.grid(row=0, column=1, padx=2, pady=2, sticky=tkinter.EW)
        self.greenButton.grid(row=0, column=2, padx=2, pady=2, sticky=tkinter.EW)
        self.blueButton.grid(row=0, column=3, padx=2, pady=2, sticky=tkinter.EW)
        self.clearButton.grid(row=0, column=4, padx=2, pady=2, sticky=tkinter.EW)
        self.undoButton.grid(row=0, column=5, padx=2, pady=2, sticky=tkinter.EW)
        self.canvas.grid(row=1, columnspan=7, padx=2, pady=2, sticky=tkinter.EW)

        self.canvas.bind("<B1-Motion>", self._mouseDragged)
        self.redButton.bind("<Button-1>", self._redPaint)
        self.greenButton.bind("<Button-1>", self._greenPaint)
        self.blueButton.bind("<Button-1>", self._bluePaint)
        self.clearButton.bind("<Button-1>", self._clearCanvas)
        self.undoButton.bind("<Button-1>", self._undoCanvas)

    def _redPaint(self,event):
        self.paintColor = "red"

    def _greenPaint(self,event):
        self.paintColor = "green"

    def _bluePaint(self,event):
        self.paintColor = "blue"

    def _clearCanvas(self, event):
        self.history.clear()
        self.canvas.delete(tkinter.ALL)

    def _undoCanvas(self, event):
        self.history.undo()
        self.canvas.delete(tkinter.ALL)
        self.history.execute()

    def _mouseDragged(self,event):
        cmd = DrawCommand(self, event, self.paintColor)
        self.history.append(cmd)
        cmd.execute()

application = tkinter.Tk()
application.title("State Samlpe")
window = CanvasFrame(application)
application.protocol("WM_DELETE_WINDOW", window.quit)
application.mainloop()