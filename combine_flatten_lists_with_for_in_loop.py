legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine'] 

#raw_db = [legacy_customers, new_customers]

#print(raw_db) 

#Return value
 #[['Alice', 'Bob'], ['Tiffany', 'Kristine']]

for legacy_customer in legacy_customers:
	new_customers.append(legacy_customer)

print(new_customers)

# Return Value
'''
['Tiffany', 'Kristine', 'Alice', 'Bob']
'''