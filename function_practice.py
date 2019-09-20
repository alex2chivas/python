def house_price(location, *args, **kwargs):
	print(f"We are going to buy houses in {location} that range from {' '.join(args)}")

	if kwargs:
		print('What is the cost?')
		for key,val in kwargs.items():
			print(f"We want this house on {key} at this price {val}")


house_price(	'Lancaster',
				'150,000',
				'250,000',
				Ave_I = '175,000',
				Ave_H = '185,000',
				Ave_G = '205,000',
				Ave_K = '245,000' )
