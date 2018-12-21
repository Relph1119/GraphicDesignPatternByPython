import tkinter


class Main(tkinter.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()

        self.checkValue = tkinter.StringVar()

        self.checkGuest = tkinter.Radiobutton(self, text="Guest", variable=self.checkValue, value="Guest",
                                              anchor=tkinter.W)
        self.checkLogin = tkinter.Radiobutton(self, text="Login", variable=self.checkValue, value="Login",
                                              anchor=tkinter.W)
        usernameLabel = tkinter.Label(self, text="Username:", anchor=tkinter.W, underline=0)
        self.textUser = tkinter.Entry(self, width=10, state="disable")
        passwordLabel = tkinter.Label(self, text="Password:", anchor=tkinter.W, underline=0)
        self.textPassword = tkinter.Entry(self, width=10, show='*', state="disable")
        self.buttonOk = tkinter.Button(self, text="OK", state="normal")
        self.buttonCancel = tkinter.Button(self, text="Cancel", command=self.quit)

        self.checkGuest.select()
        self.checkLogin.deselect()

        self.checkGuest.grid(row=0, column=0, padx=2, pady=2,
                             sticky=tkinter.W)
        self.checkLogin.grid(row=0, column=1, padx=2, pady=2,
                             sticky=tkinter.EW)
        usernameLabel.grid(row=1, column=0, padx=2, pady=2,
                           sticky=tkinter.W)
        self.textUser.grid(row=1, column=1, padx=2, pady=2,
                           sticky=tkinter.EW)
        passwordLabel.grid(row=2, column=0, padx=2, pady=2,
                           sticky=tkinter.W)
        self.textPassword.grid(row=2, column=1, padx=2, pady=2,
                               sticky=tkinter.EW)
        self.buttonOk.grid(row=3, column=0, padx=2, pady=2,
                           sticky=tkinter.EW)
        self.buttonCancel.grid(row=3, column=1, padx=2, pady=2,
                               sticky=tkinter.EW)

        self.checkGuest.focus_set()

        self.checkGuest.bind("<Button-1>", self.checkChange)
        self.checkLogin.bind("<Button-1>", self.checkChange)

        self.textUser.bind("<Key>", self.checkChange)
        self.textPassword.bind("<Key>", self.checkChange)

    def checkChange(self, event):
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


if __name__ == '__main__':
    application = tkinter.Tk()
    application.title("Mediator Sample")
    window = Main(application)
    application.protocol("WM_DELETE_WINDOW", window.quit)
    application.mainloop()
