players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

#copy() function is only accessed by us, if someone else is making a change it will not affect our end
player_names = list(players.copy().values())

#print(players.keys())
#print(player_names) #view objects are not True list
# add the list() function we can call it like a regular list
#print(players.items())

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" : ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}


team_grouping = teams.items()
#print(len(team_grouping))
value_one = list(team_grouping)[1][1][0]
value_two = list(team_grouping)[1][1][1]
added_value = value_one +" "+ value_two
print(added_value)

'''
link to view dictionary view objects
https://docs.python.org/3.0/library/stdtypes.html#dictionary-view-objects
'''
