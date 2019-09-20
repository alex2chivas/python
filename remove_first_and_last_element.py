
#remove_first_and_last(list_to_clean)

html = ['<h1>', 'Some Content', '</h1>' ]

#remove_first_and_last(html):
#	'some content'

html_2 = ['<h1>', 'Some Content', 'more','more','more','more', '</h1>' ]

#remove_first_and_last(html):
#	['some content', 'more']



def remove_first_and_last(list_to_clean):
	_, *content, _ = list_to_clean
	if 3 < len(content) -1:
		return content
	else:
		return ('Not greater than 3 elements')
	

print(remove_first_and_last(html))
print(remove_first_and_last(html_2))

'''
one, *two , three = [1, 2, 3, 4, 5] # *two makes an array [2, 3, 4]
print(two)

'''