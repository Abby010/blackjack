class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def getSuit(self):
        return self._suit
    
    def getValue(self):
        return self._value
    
    def print(self):
        print(f'The card is a {self.getSuit()} and its value is {self.getValue()}')

    