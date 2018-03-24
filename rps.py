# rps.py

import random

def is_valid_play(play):
	return play in ['rock', 'paper','scissors']

def random_play():
	return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
	if human == computer:
    		return 'tie'
	elif human == 'rock' and computer == 'scissors':
    		return 'human'
	elif human == 'rock' and computer == 'paper':
   		return 'computer'
	elif human == 'scissors' and computer == 'rock':
		return 'human'
	elif human == 'scissors' and computer == 'paper':
		return 'computer'
	elif human == 'paper' and computer == 'rock':
		return 'human'
	elif human == 'paper' and computer == 'scissors':
		return 'computer'
	else: 
		print(computer)

def main(input=input):
	human = ''

	while human not in ['rock', 'paper', 'scissors']:
    		human = input('rock, paper or scissors? ')

	computer = random_play()

	print(computer)

	result = determine_game_result(human, computer)
	if result == 'tie':
		print('it\'s a tie')
	else:
		print(result, 'wins')

if __name__ == '__main__':
	main()
