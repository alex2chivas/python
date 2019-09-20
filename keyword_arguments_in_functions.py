def greeting(**kwargs):
	if kwargs:
		print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day") # return dictionary {}
	else:
		print('Hi Guest')
greeting(first_name = 'Alex', last_name = 'Flores')
greeting()