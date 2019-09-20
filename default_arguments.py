'''
def greeting(name = 'Guest'): # defualt argument
  print(f'Hi {name}!')

greeting('Gabi')
greeting()
'''
#programming quesiton

def some_function(collection = []): # dangerous default value [] as argument
	collection.append(1)
	print(id(collection))  # 2305382703752 has the same memory number
	return collection


print(some_function())

# other part of the program
print(some_function()) # expected list of [1] but it is not 
					   # storing data, return [1, 1]

'''
Important do not set list at default value!!!!!!!!!
bad Practice
'''