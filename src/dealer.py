class Dealer(Player):
    def __init__(self, hand):
        super().__init__(hand)
        self._targetScore = 17

    def updateTargetScore(self, score):
        self._targetScore = score

    def makeMove(self):
        return self.getHand().getScore() < self._targetScore