# Not recomended to use a lot, simple is better


role = 'admin'
'''
auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)
'''

if role == 'admin':
	auth = 'can access'
else:
	auth ='can not access'

print(auth)