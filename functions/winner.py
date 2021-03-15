from random import choice
from functools import reduce

def declare_winner(player_hand, dealer_hand, deck):
    player_score = reduce(lambda a, b: a + b, player_hand)
    dealer_score = reduce(lambda a, b: a + b, dealer_hand)

    print(f"Player hand {player_hand}({player_score})")
    print(f"Dealer hand {dealer_hand}({dealer_score})")

    if player_score == 21:
        return "\n** YOU HIT A BLACK JACK **\n** YOU WON! **"

    if player_score > 21:
        return "\n** BUST **\n YOU LOSE!"

    while dealer_score < 17:
        drawn_card = choice(deck)
        dealer_hand.append(drawn_card)
        dealer_score += drawn_card

        print("Dealer's hand is less than 17. He must draw a card...")
        print(f"Dealer draws {drawn_card}.\nDealer's hand is now {dealer_hand} ({dealer_score}).\n")

    if player_score == dealer_score:
        return "\n** DRAW **"

    if dealer_score > 21:
        return "\n** YOU WON! **"

    if player_score > dealer_score:
        return "\n** PLAYER WON! **"
    else:
        return "\n** DEALER WON! **"

