from replit import clear

from random import shuffle
from functools import reduce

from functions.starting_hand import draw_starting_hands
from functions.winner import declare_winner

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []

def game_init():
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

