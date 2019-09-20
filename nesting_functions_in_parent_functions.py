def greeting(first, last):
	def full_name():
		return f'{first} {last}'

	print(f'Hi {full_name()}!')

greeting('Alex', 'Flores')

# nest only when it does not need to excist outside of the parent function