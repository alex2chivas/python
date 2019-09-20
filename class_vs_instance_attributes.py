'''
class Website:
	def __init__(self, title):
		self.title = title # instance attributes

ws = Website('My Website Title')
print(ws.__dict__) # returns {'title': 'My Website Title'}

ws_two = Website('Second Title') # second instance/ data value specific to this instance
print(ws_two.__dict__)
'''
class DifferentWebsite:  # This is a class attribute
	title = 'My class Title'

dw = DifferentWebsite()
print(dw.__dict__) # we do not get any attribute (return {})
print(dw.title) # But you do have access to the class Attribute

dw_two = DifferentWebsite()
print(dw_two.__dict__) # we do not get any attribute (return {})
print(dw.title)