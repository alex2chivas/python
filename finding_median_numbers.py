import math
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""


sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sale_items = sorted_list[:half_slice]
last_sale_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice +1 )]


print(sorted_list)
print(num_of_sales)
print(first_sale_items)
print(last_sale_items)
print(median)
