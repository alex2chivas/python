tags = ['python', 'development', 'tutorials', 'code']

# Nope
#tags[-1] = 'Programming' #replaced code

#tags.extend('Programming')#spreads each letter in the word as its own list

#tags.extend(['Programming']) # adds Prgramming to the end of the list as a single list item
#extend returns none, changes tags but does not return a new value

new_tags = tags + ['Programming'] # returns a new list with the new item

print(new_tags)

print(tags)