class UserPlayer(Player):
    def __init__(self, balance, hand):
        super().__init__(hand)
        self._balance = balance

    def getBalance(self):
        return self._balance

    def placeBet(self, amount):
        if amount > self._balance:
            raise ValueError('Insufficient funds')
        self._balance -= amount
        return amount

    def receiveWinnings(self, amount):
        self._balance += amount

    def makeMove(self):
        if self.getHand().getScore() > 21:
            return False

        while True:
            move = input('🃏 Draw another card? [y/n]: ').strip().lower()
            if move in ['y', 'n']:
                return move == 'y'
            else:
                print("❗ Please enter 'y' or 'n'.")
