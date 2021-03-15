from random import choice
from functools import reduce

def declare_winner(player_hand, dealer_hand, deck):
    player_score = reduce(lambda a, b: a + b, player_hand)
    dealer_score = reduce(lambda a, b: a + b, dealer_hand)

    while dealer_score < 17:
        drawn_card = choice(deck)
        dealer_hand.append(drawn_card)
        dealer_score += drawn_card
        print("Dealer's hand is less than 17. He must draw a card...")
        print(f"Dealer draws {drawn_card}.\nDealer's hand is now {dealer_hand} ({dealer_score}).\n")

    if player_score == dealer_score:
        return f"DRAW! Your score was {player_score}\nDealer score was {dealer_score}"

    if player_score > 21:
        return f"\nYour score was {player_score}\nDealer score was {dealer_score}"


    if dealer_score > 21:
        return f"You won!\n\nYour score was {player_score}\nDealer score was {dealer_score}"

    if player_score > dealer_score:
        return f"\nYour score was {player_score}\nDealer score was {dealer_score}"

    else:
        return f"\nDealer won!\n\nDealer score was {dealer_score}\nYour score was {player_score}"