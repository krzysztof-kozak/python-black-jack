############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from replit import clear
from random import shuffle
from functools import reduce

from functions.starting_hand import draw_starting_hands

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_hand = []
player_hand = []

if input("Welcome to Black Jack\nBegin? (typ y or n) ").lower() == "y":

	shuffle(deck)
	draw_starting_hands(dealer_hand, player_hand, deck)

	clear()

	dealer_score = reduce(lambda a, b: a + b, dealer_hand)
	player_score = reduce(lambda a, b: a + b, player_hand)

	print(f"dealer's hand: {dealer_hand} | score = {dealer_score}")
	print(f"player's hand: {player_hand} | score = {player_score}")






