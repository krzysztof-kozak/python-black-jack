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

    if input("Welcome to Black Jack\nBegin?\nType y to begin or anykey to quit ").lower() == "y":
        shuffle(deck)
        draw_starting_hands(dealer_hand, player_hand, deck)

        player_score = reduce(lambda a, b: a + b, player_hand)

        if player_score == 21:
            print("\n** YOU DRAW A BLACKJACK **\n** YOU WON! **")
            return
    
        clear()

        print(f"Dealer's hand: { [dealer_hand[0], 'concealed'] }")
        print(f"Your hand: {player_hand}({player_score})")

        correct_option = False

        while not correct_option:
            hit_or_stand = input("\nHit or stand? (type h or s) ").lower()
            if hit_or_stand == "h" or hit_or_stand == "s":
                correct_option = True

        clear()

        if hit_or_stand == "s":
            winner = declare_winner(player_hand, dealer_hand, deck)
            print(winner)

        elif hit_or_stand == "h":
            hit_again = True

            while hit_again:
                player_score, player_hand, drawn_card = draw_a_card(player_hand, deck)
                print

                if player_score < 21:
                    print(f"You drew {drawn_card}...")
                    print(f"Your hand is now {player_hand}({player_score})")
                    correct_option = False

                    while not correct_option:
                        hit_or_stand = input("\nHit again or stand? type h or s: ").lower()
                        if hit_or_stand == "h" or hit_or_stand == "s":
                            correct_option = True
                else:
                    hit_again = False
                    
                    if drawn_card != 1:
                        print(f"You drew {drawn_card}...")

                    winner = declare_winner(player_hand, dealer_hand, deck)
                    print(winner)           
        return True
    else:
        return False