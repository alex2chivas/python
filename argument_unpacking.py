def greeting(time_of_day ,*args): # python convention *args
#	print('Hi, ' + time_of_day +' '.join(args))
#	print(args) # turns into tuples ('Tiffany', 'Rome', 'Martin')
	print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")

greeting( ' Morning, ' ,'Tiffany', 'Rome', 'Martin')