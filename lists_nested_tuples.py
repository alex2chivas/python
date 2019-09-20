post = ('Python Basics', 'Intro guide to python', 'Some cool python content' )

tags = ['python', 'coding', 'tutorial']

teams = {'Barcelona': {'Messi', 'Suarez', 'Neymar'}, 'Madrid': {'Benzemar', 'Luka', 'Marcelo'}}

post += (tags,)
post += (teams,)
both_teams = post[-1]
Barcelona = both_teams.get('Barcelona', 'no value')
print(Barcelona)
neymar = list(Barcelona)[-2:]

print(neymar)