class Lineup:
	def __init__(self, players):
		self.players = players
		self.last_player_index = (len(self.players) -1)

	def __iter__(self):
		self.n = 0
		return self

	def get_player(self, n):
		return self.players[n]

	def __next__(self):	
		if self.n < self.last_player_index:
			player = self.get_player(self.n)
			self.n += 1
			return player
		elif self.n == self.last_player_index:
			player = self.get_player(self.n)
			self.n = 0
			return player

astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))

'''
class Lineup:

	def __init__(self, players, goals):
		self.players = players
		self.goals = goals

	def __iter__(self):
		self.p = 0
		self.g = 0
		return self, self

	def __next__(self):
		if self.p < (len(self.players) -1) and self.g < (len(self.goals) -1):
			player = self.players[self.p]
			goal = self.goals[self.g]
			self.p += 1
			self.g += 1
			player_goal = f'{player} scored {goal}'
			return player_goal

		elif self.p == (len(self.players) -1) and (self.g == (len(self.goals) -1) or self.g > (len(self.goals) -1) ):
			player = self.players[self.p]
			goal = self.goals[self.g]
			self.p = 0
			self.g = 0
			player_goal = f'{player} scored {goal}'
			return player_goal


barcelona = [
  'Suarez',
  'Messi',
  'Neymar',
  'Pique',
  'Xavi',
  'Iniesta',
  'Dani Alves',
  'Dembele',
  'Griezman'
]

goals = [
	10,
	20,
	30,
	12
]



barcelona_lineup = Lineup(barcelona, goals)
process = iter(barcelona_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
'''