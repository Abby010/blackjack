class Hand:
    def __init__(self):
        self._cards = []
        self._score = 0

    def addCard(self, card):
        self._cards.append(card)
        if card.getValue() == 1:
            self._score += 11 if self._score + 11 <= 21 else 1
        else:
            self._score += card.getValue()
        print('Score ', self._score)

    def getScore(self):
        return self._score
    
    def getCards(self):
        return self._cards
    
    def print(self):
        table = Table(title="Hand")
        table.add_column("Card", justify="center", style="cyan", no_wrap=True)

        for card in self._cards:
            table.add_row(f"{card.getValue()} of {card.getSuit().value.capitalize()}")

        table.add_row(f"[bold green]Total Score: {self.getScore()}[/bold green]")
        console.print(table)
