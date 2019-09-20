def pretty_price(gross_price, extension):
	if isinstance(extension, int): # is this an interger
		extension *= 0.01

	return round(gross_price) + extension	


print(pretty_price(3.99, 0.99))
print(pretty_price(3.40, 99))
