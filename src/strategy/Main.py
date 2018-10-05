from Player import Player
from WinningStrategy import WinningStrategy
from ProbStrategy import ProbStrategy
import sys

def main():
    if len(sys.argv) != 3:
        usage()

    player1 = Player("Taro", WinningStrategy(sys.argv[1]))
    player2 = Player("Hana", ProbStrategy(sys.argv[2]))

    for i in range(10000):
        nextHand1 = player1.nextHand()
        nextHand2 = player2.nextHand()
        if nextHand1.is_stronger_than(nextHand2):
            print("Winner:{0}".format(player1))
            player1.win()
            player2.lose()
        elif nextHand2.is_stronger_than(nextHand1):
            print("Winner:{0}".format(player2))
            player1.lose()
            player2.win()
        else:
            print("Even...")
            player1.even()
            player2.even()

    print("Total result")
    print(player1)
    print(player2)

def usage():
    print("Usage: python {0} randomseed1 randomseed2".format(sys.argv[0]))
    print("Example: python Main.py 314 15")
    sys.exit(0)

main()
