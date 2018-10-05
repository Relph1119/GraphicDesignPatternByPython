from Display import Display

class CountDisplay(Display):
    def __init__(self, impl):
        self.impl = impl

    def multi_display(self, times):
        self.open()
        for i in range(times):
            self.print()
        self.close()
