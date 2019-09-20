full_name = lambda first, last: f"{first} {last}" #return value, functionality and pass this function quickly into other parts of the program

def greeting(name):
	print(f" Hi there {name}")

greeting(full_name('Alex', 'Flores'))