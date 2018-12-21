import tkinter
from state.DayState import DayState
from state.Context import Context
from tkinter.scrolledtext import ScrolledText


class SafeFrame(tkinter.Frame, Context):
    def __init__(self, parent, isRunning):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        self.state = DayState()
        self.isRunning = isRunning

        self.textClock = tkinter.Label(self, width=60, text="现在时间是00:00", anchor=tkinter.W)
        self.textScreen = ScrolledText(self, height=10, width=60, state="disable")
        self.buttonUse = tkinter.Button(self, text="使用金库")
        self.buttonAlarm = tkinter.Button(self, text="按下警铃")
        self.buttonPhone = tkinter.Button(self, text="正常通话")
        self.buttonExit = tkinter.Button(self, text="结束", command=self.quit)

        self.textClock.grid(row=0, columnspan=6, padx=2, pady=2, sticky=tkinter.EW)
        self.textScreen.grid(row=1, columnspan=6, padx=2, pady=2, sticky=tkinter.EW)
        self.buttonUse.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.EW)
        self.buttonAlarm.grid(row=2, column=2, padx=2, pady=2, sticky=tkinter.EW)
        self.buttonPhone.grid(row=2, column=3, padx=2, pady=2, sticky=tkinter.EW)
        self.buttonExit.grid(row=2, column=4, padx=2, pady=2, sticky=tkinter.EW)

        self.buttonUse.bind("<Button-1>", self.useEvent)
        self.buttonAlarm.bind("<Button-1>", self.useAlarm)
        self.buttonPhone.bind("<Button-1>", self.usePhone)

    def quit(self, event=None):
        self.isRunning = False
        self.parent.destroy()

    def useEvent(self, event):
        self.state.doUse(self)

    def useAlarm(self, event):
        self.state.doAlarm(self)

    def usePhone(self, event):
        self.state.doPhone(self)

    def setClock(self, hour):
        self.clockstring = "现在时间是"
        if hour < 10:
            self.clockstring += "0{0}:00".format(hour)
        else:
            self.clockstring += "{0}:00".format(hour)
        self.textClock["text"] = self.clockstring
        self.state.doClouck(self, hour)
        print(self.clockstring)

    def changeState(self, state):
        print("从{0}状态变为了{1}状态".format(self.state, state))
        self.state = state

    def callSecurityCenter(self, msg):
        self.textScreen["state"] = tkinter.NORMAL
        self.textScreen.insert(tkinter.END, "{0} call! {1}\n".format(self.clockstring, msg))
        self.textScreen.see(tkinter.END)
        self.textScreen["state"] = tkinter.DISABLED

    def recordLog(self, msg):
        self.textScreen["state"] = tkinter.NORMAL
        self.textScreen.insert(tkinter.END, "{0} record... {1}\n".format(self.clockstring, msg))
        self.textScreen.see(tkinter.END)
        self.textScreen["state"] = tkinter.DISABLED
