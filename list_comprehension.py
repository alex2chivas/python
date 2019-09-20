num_list = range(1, 11)
#cubed_nums = []

#for num in num_list:
#	cubed_nums.append(num* * 3)
 
             # value/action then for/in Loop
#cubed_nums = [num ** 3 for num in num_list]

'''
even_numbers = []

for num in num_list:
	if num % 2 == 0:
		even_numbers.append(num)
'''

even_numbers = [num * 4 for num in num_list if not num  % 2 == 2]

print(even_numbers)