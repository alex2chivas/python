'''
import numpy as np 

def weighted_lottery(weights):
	container_list = []

	for (name, weight) in weights.items():
		for _ in range(weight):
			container_list.append(name)

	return np.random.choice(container_list) # pulls a random value from the list

other_weights = {
	'winning' : 1,
	'break_even': 2,
	'losing': 3
}

print(weighted_lottery(other_weights))
'''

import numpy as np

def weighted_lottery(weights):
	container_holder = []

	for (key, value) in weights.items(): #also, key() and value()
		for _ in range(value):
			container_holder.append(key)

	return np.random.choice(container_holder)

loterry = {
	'goals': 2,
	'goal_keeper_saves': 3,
	'misses': 10
}

print(weighted_lottery(loterry))