from replit import clear

from random import shuffle
from functools import reduce

from functions.starting_hand import draw_starting_hands
from functions.winner import declare_winner


def game_init():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_hand = []
    player_hand = []

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

        hit_or_stand = input("\nHit or stand? (type h or s) ").lower()

        if hit_or_stand == "s":
            winner = declare_winner(player_score, dealer_score, deck)
            clear()
            print(winner)

        elif hit_or_stand == "h":
            print("H test")


