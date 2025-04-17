import random
from suit import Suit
from card import Card

class Deck:
    def __init__(self):
        for suit in Suit:
            for value in range(1,14):
                self._cards.append(Card(suit,min(value,10)))

    def print(self):
        for card in self._cards:
            card.print()

    def draw(self):
        return self._cards.pop()
    
    def shuffle(self):
        for i in range(len(self._cards)):
            j = random.randint(0,51)
            self._cards[i], self._cards[j] = self._cards[j], self.cards[i]