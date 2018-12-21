from Banner import Banner
from Print import Print


class PrintBanner(Banner, Print):
    def __init__(self, name):
        super().__init__(name)

    def print_weak(self):
        self.show_with_paren()

    def print_strong(self):
        self.show_with_aster()
