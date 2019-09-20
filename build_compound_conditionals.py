
'''
username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenort' 

# We can also nest the conditionals
# and needs both to be True
# or needs only one to be True / left to right 
# not turn True-False and False-True

# paren gets treated as it single line of code then it goes and searches for and 

if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth' :
	print('Access permitted')
else:
	print('You shall not pass')

'''

def access_computer():
	while True:
		print('Login Please')
		user = input()
		email = input()
		password = input()
		
		if user == ('Alex' or email == 'alex@comcast.com') and password == 'Alex02':
			print('Primary User')
			return False
		else:
			print('Try Again\n')
access_computer()


