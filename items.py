

#This will be the info about all the objects in the game.

coconut = {
    'name': 'coconut',
    'desc': "Consider the coconut!",
    'getable': True,
    'edible': True,
    'usable': False,
    'health': 5,
    'inv': 0
        }
rope = {
    'name': 'rope',
    'desc': 'Here is a wet piece of rope. It must have washed up from your wreck.',
    'getable': True,
    'edible': False,
    'usable': True,
    'health': 0,
    'inv': 0
    }
seagull = {
    'name': 'seagull',
    'desc': '''A seagull swoops in the sky, searching for food. It eyes you in a way
that makes you feel uncomfortable...''',
    'getable': False,
    'edible': True,
    'usable': False,
    'health': 8,
    'inv': 0
    }
rock = {
    'name': 'rock',
    'desc': '''Here is a sharp piece of rock. Maybe you could use it to make 
something...''',
    'getable': True,
    'edible': False,
    'usable': True,
    'health': 0,
    'inv': 0
    }
starfish = {
    'name': 'starfish',
    'desc': 'The starfish contemplates life in a rockpool...',
    'getable': True,
    'edible': True,
    'usable': True,
    'health': 6,
    'inv': 0
    }
shellfish = {
    'name': 'shellfish',
    'desc': 'A small shellfish sticks to this rocky outcrop. Looks delicious...',
    'getable': True,
    'edible': True,
    'usable': False,
    'health': 3,
    'inv': 0
    }
stick = {
    'name': 'stick',
    'desc': '''An old stick. You stare at it for a moment. You wonder about what it
could have been, and what it may yet become.''',
    'getable': True,
    'edible': False,
    'usable': False,
    'health': 0,
    'inv': 0
    }
vine = {
    'name': 'vine',
    'desc': '''You pull on a vine. It comes off in your hand. Easy to break, but may
still be useful...''',
    'getable': True,
    'edible': False,
    'usable': False,
    'health': 0,
    'inv': 0
    }
berry = {
    'name': 'berry',
    'desc': """A purple berry. You roll it in your hand. It could be delicious, but
what if it kills you instead?""",
    'getable': True,
    'edible': True,
    'usable': False,
    'health': 0,
    'inv': 0
    }
rock = {
	'name' : 'rock',
	'desc': '''Before you lies a rock. You weigh it in your hand.
Somewhere, a memory stirs inside you. This is a sedimentary rock,
the kind known as 'sandstone'....''',
	'getable': True,
	'edible': False,
	'usable': False,
	'health': 0,
	'inv': 0
	}

#This is the results of tool uses...
wood = {
    'name': 'wood',
    'desc': 'A piece of firewood. Can be used with flint and steel to make a fire.',
    'getable': False,
    'edible': False,
    'usable': False,
    'health': 0,
    'inv': 0
    }

#This is the info about the tools...
axe = {
    'name': 'axe',
    'desc': 'A makeshift axe. Looks like it can break apart at any time.',
    'getable': False,
    'edible': False,
    'usable': True,
    'health': 0,
    'ingredients': [rock, vine, stick],
    'string': '''You use the axe. The sapling falls to the ground, another defeated
foe >:). You got 1 wood.''',
    'getitem': wood,
    'settings': [5],
    'inv': 0
    }







