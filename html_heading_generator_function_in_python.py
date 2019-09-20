'''
heading_generator(title, heading_type)
heading_generator('Greeting', 1)
<h1>Greeting</h1>

heading_generator('Hi there', 3)
<h3>Hi there</h3>

'''
'''
def heading_generator(title, heading_type):
	heading = {
		1: 'h1',
		2: 'h2',
		3: 'h3',
		4: 'h4',
		5: 'h5',
		6: 'h6',
	}

	heading_type = heading.get(heading_type, 'no value')

	return f'<{heading_type}>{title}</{heading_type}>'

h1_tag = heading_generator('Hello World', 1)
print(h1_tag)

h2_tag = heading_generator('Hello', 2)
print(h2_tag)

h3_tag = heading_generator('World', 3)
print(h3_tag)

h4_tag = heading_generator('Hi There', 4)
print(h4_tag)

h5_tag = heading_generator('Hi', 5)
print(h5_tag)

h6_tag = heading_generator('Hey There', 6)
print(h6_tag)
'''
def heading_generator(title, heading_type):
	return f'<h{heading_type}>{title}</h{heading_type}>'

print(heading_generator('Hello World I am Alexis', 2))

h6_tag = heading_generator('Hey There', 6)
print(h6_tag)