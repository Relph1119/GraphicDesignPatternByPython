import tkinter
from mediator.ConcreteColleague import ColleagueButton, ColleagueEntry, ColleagueRadiobutton
from mediator.Mediator import Mediator


class Main(tkinter.Frame, Mediator):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        self.checkValue = tkinter.StringVar()

        self.createColleagues()

        self.checkGuest.grid(row=0, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.checkLogin.grid(row=0, column=1, padx=2, pady=2, sticky=tkinter.EW)
        self.usernameLabel.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.textUser.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.EW)
        self.passwordLabel.grid(row=2, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.textPassword.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.EW)
        self.buttonOk.grid(row=3, column=0, padx=2, pady=2, sticky=tkinter.EW)
        self.buttonCancel.grid(row=3, column=1, padx=2, pady=2, sticky=tkinter.EW)

        self.checkGuest.focus_set()

        self.checkGuest.bind("<Button-1>", self.colleagueChanged)
        self.checkLogin.bind("<Button-1>", self.colleagueChanged)

        self.textUser.bind("<Key>", self.colleagueChanged)
        self.textPassword.bind("<Key>", self.colleagueChanged)

    def createColleagues(self):
        self.checkGuest = ColleagueRadiobutton(self, "Guest", self.checkValue)
        self.checkLogin = ColleagueRadiobutton(self, "Login", self.checkValue)
        self.usernameLabel = tkinter.Label(self, text="Username:", anchor=tkinter.W, underline=0)
        self.textUser = ColleagueEntry(self, 10)
        self.passwordLabel = tkinter.Label(self, text="Password:", anchor=tkinter.W, underline=0)
        self.textPassword = ColleagueEntry(10, '*')
        self.buttonOk = ColleagueButton("OK")
        self.buttonCancel = ColleagueButton("Cancel", self.quit)

        self.checkGuest.setMediator(self)
        self.checkLogin.setMediator(self)
        self.textUser.setMediator(self)
        self.textPassword.setMediator(self)
        self.buttonOk.setMediator(self)
        self.buttonCancel.setMediator(self)

        self.checkGuest.setColleagueEnable(True)
        self.checkLogin.setColleagueEnable(False)

    def colleagueChanged(self):
        if self.checkValue == "Guest":
            self.textUser["state"] = "disable"
            self.textPassword["state"] = "disable"
            self.buttonOk["state"] = "normal"
        else:
            self.textUser["state"] = "normal"
            self.userpassChanged()

    def userpassChanged(self):
        if len(self.textUser.get()) > 0:
            self.textPassword["state"] = "normal"
            if len(self.textPassword.get()) > 0:
                self.buttonOk["state"] = "normal"
            else:
                self.buttonOk["state"] = "disable"
        else:
            self.textPassword["state"] = "disable"
            self.buttonOk["state"] = "disable"

    def quit(self, event=None):
        self.parent.destroy()


application = tkinter.Tk()
application.title("Mediator Sample")
window = Main(application)
application.protocol("WM_DELETE_WINDOW", window.quit)
application.mainloop()
