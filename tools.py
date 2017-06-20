import items
import rooms

#This is the info about the tools...
axe = {
    'name': 'axe',
    'desc': 'A makeshift axe. Looks like it can break apart at any time.',
    'getable': False,
    'edible': False,
    'usable': True,
    'health': 0,
    #'ingredients': [rock, vine, stick],
    'string': 'You use the axe. The sapling falls to the ground, another defeated foe >:). You got 1 wood.',
    'getitem': wood,
    'settings': [5],
    'inv': 0
    }

toolslist = [axe]
