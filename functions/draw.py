from random import choice
from functools import reduce
from replit import clear

def draw_a_card(player_hand, deck):
    drawn_card = choice(deck)
    clear()
    if drawn_card == 11:
        print("You drew an ACE!")
        print("Calculating the optimal strategy...")

        if reduce(lambda a, b: a + b, player_hand) + drawn_card > 21:
            drawn_card = 1
            print("Changing ACE to 1...")
        else:
            print("Changing ACE to 11...")

    player_hand.append(drawn_card)
    player_score = reduce(lambda a, b: a + b, player_hand)

    
    return player_score, player_hand, drawn_card