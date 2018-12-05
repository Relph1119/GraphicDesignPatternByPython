from RandomNumberGenerator import RandomNumberGenerator
from DigitObserver import DigitObserver
from GraphObserver import GraphObserver

if __name__ == '__main__':
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.addObserver(observer1)
    generator.addObserver(observer2)
    generator.execute()
