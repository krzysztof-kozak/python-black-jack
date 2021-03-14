from random import choice

def draw_starting_hands(dealer, player, deck):
	for i in range(0, 2):
		random_card = choice(deck)
		dealer.append(random_card)
		
		random_card = choice(deck)
		player.append(random_card)