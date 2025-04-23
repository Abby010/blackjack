from ui import print_title_screen
from userPlayer import UserPlayer
from hand import Hand
from dealer import Dealer
from deck import Deck
from gameRound import GameRound

def main():
    print_title_screen()

    # Create player and dealer with fresh hands
    player = UserPlayer(balance=100, hand=Hand())
    dealer = Dealer(hand=Hand())

    while True:
        deck = Deck()
        game = GameRound(player, dealer, deck)
        game.play()

        again = input("\n🔁 Play another round? [y/n]: ").strip().lower()
        while again not in ['y', 'n']:
            again = input("❗ Invalid input. Enter 'y' or 'n': ").strip().lower()

        if again == 'n':
            print("👋 Thanks for playing Blackjack! See you next time.")
            break

if __name__ == "__main__":
    main()
