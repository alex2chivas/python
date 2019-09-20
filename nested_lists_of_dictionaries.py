import random

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  },
  {
    'rockets': {
       'RT': 'Rob',
       'FB': 'Ricker'
    }
  },
  {
    'mets': {
       'BT': 'Timeer',
       'CK': 'Footer'
    }
  }

]

ran = random.randint(0, 2)
ran_1 = random.randint(0, 1)

astros = teams[0].get('astros', 'Team not found')
angels = teams[1].get('angels', 'Team not found')
rockets = teams[2].get('rockets', 'Team not found')
random_team = teams[ran].get('mets', 'Team not found')


print(list(astros.values())[ran])
print(list(angels.values())[ran_1])
print(list(rockets.values())[ran_1])
print(random_team)