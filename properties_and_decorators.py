class Invoice:

	def __init__(self, client, total):
		self.__client = client # private 
		self._total = total # protective

	def formatter(self):
		return f'{self.__client} owes: ${self._total}.'

	@property #clear distinction that most likely I want to access this data at some point of the program
	def client(self):
		return self.__client

	@client.setter # switch the value outside the class data point
	def client(self, client):
		self.__client = client
	
	@property # getter
	def total(self):
		return self._total 
	
	
google = Invoice('Google', 100)
print(google.client)
google.client = 'Twitch'
print(google.client)


'''
class Names:

	def __init__(self, name, city, age):
		self._name = name
		self._city = city
		self._age = age

	def combined(self):
		return f'Hello, my name is {self._name}. I am {self._age} and grew up in  {self._city}.'

	@property
	def age(self):
		return self._age

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def city(self):
		return self._city
	

alexis = Names('Alex', 'Burbank', 26)
print(alexis.combined())
'''
