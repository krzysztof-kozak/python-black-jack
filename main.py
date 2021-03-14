############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from replit import clear
from random import shuffle
from functools import reduce

from functions.starting_hand import draw_starting_hands
from functions.winner import declare_winner

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []

play_again = True

while play_again:

    clear()

    if input("Welcome to Black Jack\nBegin? (type y or n) ").lower() == "y":

        shuffle(deck)
        draw_starting_hands(dealer_hand, player_hand, deck)

        clear()

        dealer_score = reduce(lambda a, b: a + b, dealer_hand)
        player_score = reduce(lambda a, b: a + b, player_hand)

        print(f"Dealer's hand: { [dealer_hand[0], 'concealed'] }")
        print("Dealer score: unknown\n")

        print(f"Your hand: {player_hand}")
        print(f"Your score: {player_score}")

        if input("\nHit or stand? (type h or s) ") == "s":
            winner = declare_winner(player_score, dealer_score, deck)
            clear()
            print(winner)

    if input("Play again? (type y or n) ").lower() != "y":
        play_again = False