from functools import reduce
import operator

'''

names = ('Alex', 'Frank', 'Dave', 'Robert')

names = names[:1]

print(names)

'''
'''
soccer_teams = [

	{
		'Barcelona': {
				'LW': 'Messi', 
				'CF': 'Saurez', 
				'MF': 'Neymar'
			}
	},
	{
		'Real Madrid': 
			{
				'LB': 'Marcelo', 
				'MF': 'Modric', 
				'CDM': 'Casemiro' 
			}
	},
	{
		'Manchester United': 
			{
				'CB': 'Smalling', 
				'RW': 'Rashford', 
				'MF': 'Pogba' 
			}
	}
]

barcelona = soccer_teams[0]
barcelona_players = barcelona.get('Barcelona', 'No team found') 
messi = barcelona_players.get('LW', 'No player found')

print(messi)
'''

'''
def new_library(unit, op):
	operators = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
		'/': operator.truediv
	}

	return reduce((lambda total, i: operators[op](total, i)), unit)

print(new_library([23, 10, 15], '+'))
print(new_library([456, 122, 335], '-'))
''' 











