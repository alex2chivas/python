class Html():
	def __init__(self, content):
		self.content = content

	def render(self): # abstract class
		raise NotImplementedError('Subclass must implement render method')

class Heading(Html):
	def render(self):
		return f'<h1>{self.content}</h1>'

class HeadingTwo(Html):
	def render(self):
		return f'<h2>{self.content}</h2>'

class HeadingThree(Html):
	def render(self):
		return f'<h3>{self.content}</h3>'

class P(Html):
	def render(self):
		return f'<p>{self.content}</p>'

class Div(Html):
	def render(self):
		return f'<div>{self.content}</div>'




tags = [
	Div('Some content'),
	Heading('Some big Heading'),
	HeadingTwo('Another Div'),
	HeadingThree('Anothe heading'),
	P('This will contain the longest sentence in this block of code')
]

for tag in tags:
	print(tag.render())
