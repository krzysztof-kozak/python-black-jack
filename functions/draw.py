from random import choice
from functools import reduce
from replit import clear

def draw_a_card(player_hand, dealer_hand, deck):
    drawn_card = choice(deck)
    player_hand.append(drawn_card)

    player_score = reduce(lambda a, b: a + b, player_hand)

    if player_score == 21:
        clear()
        print(f"You drew {drawn_card}\nYour hand is {player_hand}({player_score})")
        print("\n ** YOU HIT A BLACKJACK **\n ** YOU WON! **\n")
        return player_score

    if player_score > 21:
        clear()
        print(f"\nYou drew {drawn_card}\nYour hand is {player_hand}({player_score})\n\n** BUST **\n** YOU LOSE! **")
        return player_score

    clear()
    print(f"You draw {drawn_card}.\nYour hand is now {player_hand}({player_score}).")
    return player_score