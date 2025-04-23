from rich.console import Console
from rich.text import Text
from rich.rule import Rule
import time

console = Console()

class GameRound:
    def __init__(self, player, dealer, deck):
        self._player = player
        self._dealer = dealer
        self._deck = deck

    def getBetUser(self):
        while True:
            try:
                amount = int(input('💰 Enter a bet amount: '))
                if amount <= 0:
                    console.print("[red]Please enter a positive number.[/red]")
                    continue
                return amount
            except ValueError:
                console.print("[red]Invalid input! Please enter a valid number.[/red]")

    def dealInitialCards(self):
        for _ in range(2):
            self._player.addCard(self._deck.draw())
            time.sleep(0.5)
            self._dealer.addCard(self._deck.draw())
            time.sleep(0.5)

        
        console.rule("[bold blue]🃏 Your Hand")
        self._player.getHand().print()

        dealerCard = self._dealer.getHand().getCards()[0]
        console.rule("[bold red]🧑‍⚖️ Dealer's Visible Card")
        console.print(f"[red]{dealerCard.getValue()} of {dealerCard.getSuit().value.capitalize()}[/red]")

    def cleanupRound(self):
        self._player.clearHand()
        self._dealer.clearHand()
        console.print(f"[bold blue]💵 Player balance: {self._player.getBalance()}[/bold blue]")

    def play(self):
        self._deck.shuffle()

        if self._player.getBalance() <= 0:
            console.print("[bold red]Player has no more money. Game over![/bold red]")
            return
        
        userBet = self.getBetUser()
        self._player.placeBet(userBet)

        self.dealInitialCards()

        # Player's turn
        while self._player.makeMove():
            time.sleep(0.5)
            drawnCard = self._deck.draw()
            console.print(f"[green]You draw: {drawnCard.getValue()} of {drawnCard.getSuit().value.capitalize()}[/green]")
            self._player.addCard(drawnCard)
            console.print(f"[bold green]Current score: {self._player.getHand().getScore()}[/bold green]")


        if self._player.getHand().getScore() > 21:
            console.print("[bold red]💥 You busted![/bold red]")
            self.cleanupRound()
            return
        
        # Dealer's turn
        console.rule("[bold red]Dealer's Turn")
        while self._dealer.makeMove():
            time.sleep(0.5)
            card = self._deck.draw()
            self._dealer.addCard(card)
            console.print(f"[red]Dealer draws: {card.getValue()} of {card.getSuit().value.capitalize()}[/red]")


        player_score = self._player.getHand().getScore()
        dealer_score = self._dealer.getHand().getScore()

        # Determine result
        console.rule("[bold yellow]🎯 Result")
        if dealer_score > 21 or player_score > dealer_score:
            console.print("[bold green]🎉 You win![/bold green]")
            self._player.receiveWinnings(userBet * 2)
        elif dealer_score > player_score:
            console.print("[bold red]💸 You lost![/bold red]")
        else:
            console.print("[bold yellow]🤝 It's a draw![/bold yellow]")
            self._player.receiveWinnings(userBet)

        self.cleanupRound()
