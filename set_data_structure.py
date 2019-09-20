tags = {
	'python',
	'coding',
	'tutorials'
	'coding' # it will not print another coding
} 
# set object requires that all the elements are unique

#print(tags)

#Nope
#print(tags[0])

query_one = 'python' in tags
print(query_one) # returns True not the actual value

query_two = 'coding' in tags
print(query_two)

query_three = 'ruby' in tags
print(query_three)