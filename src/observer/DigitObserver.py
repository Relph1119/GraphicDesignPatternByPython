from Observer import Observer


class DigitObserver(Observer):
    def update(self, generator):
        print("DigitObserver: {0}".format(generator.getNumber()))
