"""
User Database Query
Kristine
Tifanny
Alexis
"""

users = ['Kristine', 'Tifanny', 'Alexis']

print(users)

users.insert(2, 'Anthony') # choose the position

print(users)

users.append('Roberto') # name gets added at the end

print(users)

print(users[2])#return one data, not a list any more
print([users[2]])#returns a list of single data

users[4] = '' # this does not change the string insde the list
print(users) #we are just reassigning certain value
