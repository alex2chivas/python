post = ('Python Basics', 'Intro guide to python', 'Some cool python content' )

print(id(post)) #specific in memory 
print(id(post)) #specific in memory 

post += ('published',) # be treated little a mathematical expression must add a ,
#leverage reassignment, making a new Tuple. Since Tuples are immutable
print(id(post)) # creates a new object in memory
#title, sub_heading, content, status = post

#print(title)
#print(sub_heading)
#print(content)
#print(status)