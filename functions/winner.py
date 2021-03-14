from random import choice

def declare_winner(player_score, dealer_score, deck):
    if player_score > 21:
        return f"BUST. You lose\nYour score was {player_score}\nDealer score was {dealer_score}"

    while dealer_score < 17:
        dealer_score += choice(deck)
        if dealer_score > 21:
            return f"You won!\nYour score was {player_score}\nDealer score was {dealer_score}"

    if player_score > dealer_score:
        return f"You won!\nYour score was {player_score}\nDealer score was {dealer_score}"

    else:
        return f"Dealer won!\nDealer score was {dealer_score}\nYour score was {player_score}"