HANDVALUE_GUU = 0
HANDVALUE_CHO = 1
HANDVALUE_PAA = 2

name = ["石头", "剪刀", "布"]

class Hand:
    def __init__(self, handvalue):
        self.handvalue = handvalue

    @staticmethod
    def get_hand(handvalue):
        return hand[handvalue]

    def is_stronger_than(self, h):
        return self.fight(h) == 1

    def is_weaker_than(self, h):
        return self.fight(h) == -1

    def fight(self, h):
        if self == h:
            return 0
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1

    def __str__(self):
        return name[self.handvalue]

hand = [Hand(HANDVALUE_GUU), Hand(HANDVALUE_CHO), Hand(HANDVALUE_PAA)]
