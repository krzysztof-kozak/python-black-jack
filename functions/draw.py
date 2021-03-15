from random import choice
from functools import reduce

def draw_a_card(player_hand, dealer_hand, deck):
    drawn_card = choice(deck)
    player_hand.append(drawn_card)

    player_score = reduce(lambda a, b: a + b, player_hand)
    
    print(f"You draw {drawn_card}.\nYour hand is now {player_hand}({player_score}).")