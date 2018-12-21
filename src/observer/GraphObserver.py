from Observer import Observer


class GraphObserver(Observer):
    def update(self, generator):
        print("GraphObserver:", end='')
        count = generator.getNumber()
        for i in range(count):
            print("*", end='')
        print("")
