teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

featured_team = teams.get('astros', 'No Futured team')# best practice

print(featured_team)