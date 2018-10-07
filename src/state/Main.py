import tkinter
from state.SafeFrame import SafeFrame
from threading import Timer
import time

def clockStart(window):
    while True:
        for i in range(24):
            if window.isRunning:
                window.setClock(i)
                time.sleep(1)
            else:
                break

isRunning = True
application = tkinter.Tk()
application.title("State Samlpe")
window = SafeFrame(application, isRunning)

timer = Timer(2, clockStart, args=(window,))
timer.start()

application.protocol("WM_DELETE_WINDOW", window.quit)
application.mainloop()