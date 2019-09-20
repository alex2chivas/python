usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

#Continue/Break

for username in usernames:
	if username == 'cersei':
		print(f'Sorry, {username}, you are not allowed')
		continue # even though it is true continue will keep going through the loop without stopping
	else:
		print(f'{username} is allowed')


for username in usernames:
	if username == 'cersei':
		print(f'Sorry, {username}, was found at index {usernames.index(username)}')
		break # will stop execution after True 
	else:
		print(f'{username} is allowed')