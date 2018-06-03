import os
#Give program information on the general setting of the game
num_players = input("How many players: ")
num_cards = input("How many cards: ")

#Declares all the lists and dictionaries needed to keep track of the information. This is essentially the programmed version of the clue sheet and the cards held within your hands. 
cards = []
guesses = []
players = []
characters = ['mustard', 'plum', 'green', 'peacock', 'scarlet', 'white']
weapons = ['knife', 'candlestick', 'pistol', 'poison', 'trophy', 'rope', 'bat', 'ax', 'dumbbell']
rooms = ['hall', 'dining room', 'kitchen', 'patio', 'observatory', 'theater', 'living room', 'spa', 'guest house']

#all_cards = {'mustard':0, 'plum':0, 'green':0, 'peacock':0, 'scarlet':0, 'white':0, 'knife':0, 'candlestick':0, 'pistol':0, 'poison':0, 'trophy':0, 'rope':0, 'bat':0, 'ax':0, 'dumbbell':0, 'hall':0, 'dining room':0, 'kitchen':0, 'patio':0, 'observatory':0, 'theater':0, 'living room':0, 'spa':0, 'guest house':0}

character_cards = {'mustard':0, 'plum':0, 'green':0, 'peacock':0, 'scarlet':0, 'white':0}

weapon_cards = {'knife':0, 'candlestick':0, 'pistol':0, 'poison':0, 'trophy':0, 'rope':0, 'bat':0, 'ax':0, 'dumbbell':0}

room_cards = {'hall':0, 'dining room':0, 'kitchen':0, 'patio':0, 'observatory':0, 'theater':0, 'living room':0, 'spa':0, 'guest house':0}

not_owned = {'mustard':[], 'plum':[], 'green':[], 'peacock':[], 'scarlet':[], 'white':[], 'knife':[], 'candlestick':[], 'pistol':[], 'poison':[], 'trophy':[], 'rope':[], 'bat':[], 'ax':[], 'dumbbell':[], 'hall':[], 'dining room':[], 'kitchen':[], 'patio':[], 'observatory':[], 'theater':[], 'living room':[], 'spa':[], 'guest house':[]}

possibly_owned = {'mustard':[], 'plum':[], 'green':[], 'peacock':[], 'scarlet':[], 'white':[], 'knife':[], 'candlestick':[], 'pistol':[], 'poison':[], 'trophy':[], 'rope':[], 'bat':[], 'ax':[], 'dumbbell':[], 'hall':[], 'dining room':[], 'kitchen':[], 'patio':[], 'observatory':[], 'theater':[], 'living room':[], 'spa':[], 'guest house':[]}

#Program prompts for cards held in hands.
for i in range(int(num_cards)):
	entercards = input("Enter card name: ")
	cards.append(entercards)

print(cards)

#Program assigns the cards to be held by 'E'. This is the equivalent of marking down that you own the cards in your hand on the clue sheet. Currently hardcoded to auto assign them to *me* specifically, although this can be changed later and I don't think anyone else is going to use this.
for card in cards:
	if card in characters:
		character_cards[card] = 'E'
	elif card in weapons:
		weapon_cards[card] = 'E'
	elif card in rooms:
		room_cards[card] = 'E'

#Gives program the order and names of the other players. The order that the players are entered in determines play order.
for i in range(int(num_players)):
	player_names = input("Enter player names in order (1 char): ")
	players.append(player_names)
	
print(players)

#Called by the turn() function. Used to determine who couldn't respond to the accusation and markes them down as not having the cards used in the accusation. 
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
	elif index_guesser == index_disprover:
		temp_player_list = players
		del temp_player_list[index_guesser]
		do_not_have = temp_player_list
	else:
		print("This message should never appear")

#"Cleans" the data. This solves the problem of accidentally having someone listed multiple times as not having a card.
def data_cleaner():
	for key in not_owned:
		new_list = []
		for i in not_owned[key]:
			if i not in new_list:
				new_list.append(i)
		not_owned[key] = new_list
	#not currently cleaning possibly owned, as more data in possibly owned probably correlates to higher chance of containing said card.

#Because the guess strings are a mess unless printed properly
def guess_string_cleaner(guesser, character, weapon, room, disprover):
	if len(character) < 7:
		spaces = 7 - len(character)
		for i in range(0, spaces):
			character = character + ' '
	if len(weapon) < 11:
		spaces = 11 - len(weapon)
		for i in range(0, spaces):
			weapon = weapon + ' '
	if len(room) < 11:
		spaces = 11 - len(room)
		for i in range(0, spaces):
			room = room + ' '
	guess = '|Guesser: ' + guesser + ' |Character: ' + character + ' |Weapon: ' + weapon + ' | Disprover: ' + disprover + ' |'

#Because the cluesheet is also a mess if not printed properly
def cluesheet():
	for item in sorted(character_cards):
		print('-----------------------')
		edited_item = item
		if len(edited_item) < 11:
			spaces = 11 - len(edited_item)
			for i in range(0, spaces):
				edited_item = edited_item + ' '
		if character_cards[item] == 0:
			print('| ' + edited_item + ' |   |   |')
		else:
			print('| ' + edited_item + ' | X | ' + character_cards[item] + ' |')
	print('-----------------------')
	for item in sorted(weapon_cards):
		print('-----------------------')
		edited_item = item
		if len(edited_item) < 11:
			spaces = 11 - len(edited_item)
			for i in range(0, spaces):
				edited_item = edited_item + ' '
		if weapon_cards[item] == 0:
			print('| ' + edited_item + ' |   |   |')
		else:
			print('| ' + edited_item + ' | X | ' + weapon_cards[item] + ' |')
	print('-----------------------')
	for item in sorted(room_cards):
		print('-----------------------')
		edited_item = item
		if len(edited_item) < 11:
			spaces = 11 - len(edited_item)
			for i in range(0, spaces):
				edited_item = edited_item + ' '
		if room_cards[item] == 0:
			print('| ' + edited_item + ' |   |   |')
		else:
			print('| ' + edited_item + ' | X | ' + room_cards[item] + ' |')
	print('-----------------------')

#The heart of the program. 
def turn():
	game_on = True
	while game_on:
		user_input = input("Perform an action: ")
		if user_input == 'addknown':
			add_known_card_input = input("which card: ")
			add_known_person_input = input("which person, put self if pool / etc: ")
			if add_known_card_input in characters:
				character_cards[add_known_card_input] = add_known_person_input
			elif add_known_card_input in weapons:
				weapon_cards[add_known_card_input] = add_known_person_input
			elif add_known_card_input in rooms:
				room_cards[add_known_card_input] = add_known_person_input
		elif user_input == 'edit':
			edit_input_card = input("Which entry would you like to edit: ")
			edit_input_person = input("What do you want the entry to say, 0 for reset: ")
			if edit_input_card in characters:
				character_cards[edit_input_card] = edit_input_person
			elif edit_input_card in weapons:
				weapon_cards[edit_input_card] = edit_input_person
			elif edit_input_card in rooms:
				room_cards[edit_input_card] = edit_input_person
		elif user_input == 'guess':
			guesser_input = input("Which player is guessing: ")
			character_input = input("Character: ")
			weapon_input = input("Weapon: ")
			room_input = input("Room: ")
			disproven_input = input("Disproven by (type c before name if ended via card / etc): ")

			guess_string = guess_string_cleaner(guesser_input, character_input, weapon_input, room_input, disproven_input)
			guesses.append(guess_string)
			
			players_who_dont_have = disproven_solver(guesser_input, disproven_input)
			if not players_who_dont_have == None:
				not_owned[character_input].extend(players_who_dont_have)
				not_owned[weapon_input].extend(players_who_dont_have)
				not_owned[room_input].extend(players_who_dont_have)

			possibly_owned[character_input].extend(disproven_input)
			possibly_owned[weapon_input].extend(disproven_input)
			possibly_owned[room_input].extend(disproven_input)

			data_cleaner()
		elif user_input == 'end':
			are_you_sure = input("Are you sure? y/n: ")
			if are_you_sure == 'y' or 'yes':
				game_on = False
			else:
				pass
		elif user_input == 'viewdata':
			view_which_data = input("Which data?: ")
			if view_which_data == 'cards':
				print(character_cards)
				print(weapon_cards)
				print(room_cards)
			elif view_which_data == 'notowned':
				print(not_owned)
			elif view_which_data == 'possiblyowned':
				print(possibly_owned)
			elif view_which_data == 'guesses':
				for guess in guesses:
					print(guess)
		elif user_input == 'clear':
			os.system('clear')
		elif user_input == 'cluesheet':
			cluesheet()
turn()
