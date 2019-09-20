post = ('Python Basics', 'Intro guide to python', 'Some cool python content' )
#post = ['Python Basics', 'Intro guide to python', 'Some cool python content' ]
# unpacking can also work for a list
# Tuple: immutable ()
#List: mutable []

#post.sort() #can not sort Tuple, gives error

title, sub_head, content = post

print(title)
print(sub_head)
print(content)