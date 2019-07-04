class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()
class NumberCard(Card):
    def __init__(self, rank, suit):
        return super().__init__(str(rank), suit)
    def _points(self):
        return int(self.hard),int(self.soft)
class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__('A', suit)
    def _points(self):
        self.hard = 1
        self.soft = 10
class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11 : 'J', 12 : 'Q', 13 : 'K'}[rank], suit)
    def _points(self):
        self.hard = 10
        self.soft = 10
def card(rank, suit):
    if rank == 1: return AceCard(rank, suit)
    elif 2 <= rank < 11: return NumberCard(rank, suit)
    elif 11 <= rank < 14: return FaceCard(rank, suit)
    else:
        raise Exception("rank out of range!")

a = card(2, 1)
print("hello world")