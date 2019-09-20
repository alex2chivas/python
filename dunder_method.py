class Invoice:
	def __init__(self, client, total):
		self.client = client
		self.total = total


	def __str__(self): # usually for debugging purpose/for clean sentence
		return f'Invoice from {self.client} for {self.total}'

	def __repr__(self): # usually used for true raw data
		return f'Invoice <value: client: {self.client}, total: {self.total}>'

inv = Invoice('Twitch', 500)
print(str(inv))
print(repr(inv))