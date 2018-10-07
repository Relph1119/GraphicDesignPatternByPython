from mediator.Colleague import Colleague
import tkinter
from mediator.Mediator import Mediator

class ColleagueButton(Colleague, tkinter.Button):
    def __init__(self, text, command=None):
        self.button = tkinter.Button(self, text=text, command=command)

    def setMediator(self, mediator):
        self.mediator = self

    def setColleagueEnable(self, enable):
        if enable:
            self.button["state"] = "normal"
        else:
            self.button["state"] = "disable"

class ColleagueRadiobutton(tkinter.Radiobutton, Colleague):
    def __init__(self, master ,text, variable):
        self.radiobutton = tkinter.Radiobutton(self, master, text=text, variable=variable, value=text, anchor=tkinter.W)

    def setMediator(self, mediator):
        self.mediator = self

    def setColleagueEnable(self, enable):
        if enable:
            self.radiobutton.select()
        else:
            self.radiobutton.deselect()

class ColleagueEntry(Colleague, tkinter.Entry):
    def __init__(self, width, show=None):
        self.entry = tkinter.Entry(self, width=width, show=show)

    def setMediator(self, mediator):
        self.mediator = self

    def setColleagueEnable(self, enable):
        if enable:
            self.entry["state"] = "normal"
        else:
            self.entry["state"] = "disable"

