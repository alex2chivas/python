"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
	"Google": 36,
	"Facebook": 39,
	"Twitter": 15,
	"Offline": 5
}


print( 'G ' + sales.get("Google", "no value") * '$')
print( 'F ' + sales.get("Facebook", "no value") * '$')
print( 'F ' + sales.get("Twitter", "no value") * '$')
print( 'O ' + sales.get("Offline", "no value") * '$')