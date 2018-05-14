num_players = input("How many players: ")
num_cards = input("How many cards: ")
cards = []
guesses = []
players = []

all_cards = {'mustard':0, 'plum':0, 'green':0, 'peacock':0, 'scarlet':0, 'white':0, 'knife':0, 'candlestick':0, 'pistol':0, 'poison':0, 'trophy':0, 'rope':0, 'bat':0, 'ax':0, 'dumbbell':0, 'hall':0, 'dining room':0, 'kitchen':0, 'patio':0, 'observatory':0, 'theater':0, 'living room':0, 'spa':0, 'guest house':0}

not_owned = {'mustard':[], 'plum':[], 'green':[], 'peacock':[], 'scarlet':[], 'white':[], 'knife':[], 'candlestick':[], 'pistol':[], 'poison':[], 'trophy':[], 'rope':[], 'bat':[], 'ax':[], 'dumbbell':[], 'hall':[], 'dining room':[], 'kitchen':[], 'patio':[], 'observatory':[], 'theater':[], 'living room':[], 'spa':[], 'guest house':[]}

possibly_owned = {'mustard':[], 'plum':[], 'green':[], 'peacock':[], 'scarlet':[], 'white':[], 'knife':[], 'candlestick':[], 'pistol':[], 'poison':[], 'trophy':[], 'rope':[], 'bat':[], 'ax':[], 'dumbbell':[], 'hall':[], 'dining room':[], 'kitchen':[], 'patio':[], 'observatory':[], 'theater':[], 'living room':[], 'spa':[], 'guest house':[]}

for i in range(int(num_cards)):
	entercards = input("Enter card name: ")
	cards.append(entercards)

print(cards)

for card in cards:
	all_cards[card] = 'E'

for i in range(int(num_players)):
	player_names = input("Enter player names in order (1 char): ")
	players.append(player_names)
	
print(players)

def disproven_solver(guesser, disprover):
	index_guesser = players.index(guesser)
	index_disprover = players.index(disprover)
	if index_guesser < index_disprover:
		if index_guesser + 1 == index_disprover:
			pass
		else:
			do_not_have = players[index_guesser + 1:index_disprover]
			return do_not_have
	elif index_guesser > index_disprover:
		do_not_have = players[index_guesser+1:] + players[:index_disprover]
		return do_not_have
	else:
		print("This message should never appear")
def turn():
	game_on = True
	while game_on:
		user_input = input("Perform an action: ")
		if user_input == 'addknown':
			add_known_card_input = input("which card: ")
			add_known_person_input = input("which person, put self if pool / etc: ")
			all_cards[add_known_card_input] = add_known_person_input
		elif user_input == 'edit':
			edit_input_card = input("Which entry would you like to edit: ")
			edit_input_person = input("What do you want the entry to say, 0 for reset: ")
			all_cards[edit_input_card] = edit_input_person
		elif user_input == 'guess':
			guesser_input = input("Which player is guessing: ")
			character_input = input("Character: ")
			weapon_input = input("Weapon: ")
			room_input = input("Room: ")
			disproven_input = input("Disproven by (type c before name if ended via card / etc): ")

			guess_string = "|Guesser: " + guesser_input + " |Character: " + character_input + " |Weapon: " + weapon_input + " |Room: " + room_input + " |Disproven: " + disproven_input
			guesses.append(guess_string)
			
			players_who_dont_have = disproven_solver(guesser_input, disproven_input)

			not_owned[character_input] = players_who_dont_have
			not_owned[weapon_input] = players_who_dont_have
			not_owned[room_input] = players_who_dont_have

		elif user_input == 'end':
			are_you_sure = input("Are you sure? y/n: ")
			if are_you_sure == 'y' or 'yes':
				game_on = False
			else:
				pass

turn()
