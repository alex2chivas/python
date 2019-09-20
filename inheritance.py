class User:
	def __init__(self, email, first_name, last_name):
		self.email = email
		self.first_name = first_name
		self.last_name = last_name

	def greeting(self):
		return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User): # Admin get access with Parent but the parent user in this case will not have access to the child since it is not a admin
	def active_users(self):
		return '500'

tiffany = AdminUser('tif@csb.com', 'Tif', 'Runner')

savy = User('savy@msn.com', 'Savy', 'Frin')

print(tiffany.active_users())
print(savy.active_users()) 