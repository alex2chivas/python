class Heading:
	def __init__(self, content):
		self.content = content

	def render(self):
		return f'<h1>{self.content}</h1>'

class Div:
	def __init__(self, content):
		self.content = content

	def render(self):
		return f'<div>{self.content}</div>'

class P:
	def __init__(self, content):
		def render(self):
			return f'<p>{self.content}</p>'





div_one = Div('Some content')
heading = Heading('Some big Heading')
div_two = Div('Another div')
paragraph = P('Long piece of work in here, said the Joker')

def html_render(tag_object):
	print(tag_object.render())

html_render(div_one)
html_render(div_two)
html_render(heading)
html_render(paragraph)

# Use this if there is lots of shared behavior use Inheritance from the previous one
# If you do not have a lot of shared behavior then use this method 

