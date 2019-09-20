teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

remove_team = teams.pop('met', 'No team found by that name') # pop() return a value
#del teams['astros']

print(teams)
print(remove_team)