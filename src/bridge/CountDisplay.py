from Display import Display


class CountDisplay(Display):

    def multi_display(self, times):
        self.open()
        for i in range(times):
            self.print()
        self.close()
