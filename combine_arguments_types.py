def greeting(time_of_day, *args, **kwargs):
	print(f"Hi {' '.join(args)}, I hope you are having a great {time_of_day}")

	if kwargs:
		print('Your task for the day are: ')
		for key, value in kwargs.items():
			print(f'{key} => {value}')


greeting (	'Morning', 
			'Alex', 
			'Flores', 
			first = 'Empty Dishwasher',
			second = 'Take the pupper outside',
			third = 'Math Homework')