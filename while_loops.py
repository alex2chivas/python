'''
nums = list(range(1, 101))

while len(nums) > 0: #prints from highest number first
	print(nums.pop())
'''

def guessing_game():
	while True:
		print('Who do I love')
		guess = input()

		if guess == 'Gabi':
			print('I do Love you!')
			return False
		else:
			print(f'No, {guess} sorry try again\n') # \n goes into a new line

guessing_game()