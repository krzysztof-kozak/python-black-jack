from replit import clear
from random import shuffle
from functools import reduce
from functions.starting_hand import draw_starting_hands
from functions.draw import draw_a_card
from functions.winner import declare_winner


def game_init():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_hand = []
    player_hand = []

    if input("Welcome to Black Jack\nBegin? (type y or n) ").lower() == "y":
        shuffle(deck)
        draw_starting_hands(dealer_hand, player_hand, deck)

        player_score = reduce(lambda a, b: a + b, player_hand)

        if player_score == 21:
            print("\n** YOU DRAW A BLACKJACK **\n ** YOU WON! **")
            return


        clear()

        print(f"Dealer's hand: { [dealer_hand[0], 'concealed'] }")
        print(f"Your hand: {player_hand}({player_score})")

        hit_or_stand = input("\nHit or stand? (type h or s) ").lower()

        clear()

        if hit_or_stand == "s":
            winner = declare_winner(player_hand, dealer_hand, deck)
            print(winner)

        elif hit_or_stand == "h":
            hit_again = True

            while hit_again:
                player_score = draw_a_card(player_hand, dealer_hand, deck)
                if player_score < 21:
                    if input("\nHit again or stand? type h or s ").lower() != "h":
                        hit_again = False
                else:
                    hit_again = False
                    winner = declare_winner(player_hand, dealer_hand, deck)
                    print(winner)