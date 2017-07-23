import copy

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
coconut1 = copy.copy(coconut)     
coconut2 = copy.copy(coconut)
coconut3 = copy.copy(coconut)

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
stick1 = copy.copy(stick)
stick2 = copy.copy(stick)
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
berry1 = copy.copy(berry)
berry2 = copy.copy(berry)
berry3 = copy.copy(berry)
berry4 = copy.copy(berry)
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
book = {
    'name': 'book',
	'desc': '''Tattered and beaten, this book seems to be ancient
beyond repair. This book may have had writing on it some point, but
the words have long since faded to become illegible.''',
    'getable': True,
	'edible': False,
	'usable': False,
	'health': 0,
	'inv': 0
	}
string = {
    'name': 'string',
	'desc': 'A length of string, made from the flax flower.',
	'getable': False,
	'edible': False,
	'usable': False,
	'health': 'N/A',
	'inv': 0
	}

bone = {
    'name': 'bone',
	'desc': 'An old bone. But then, everything has some use.',
	'getable': True,
	'edible': False,
	'usable': False,
	'health': 'N/A',
	'inv': 0
	}
starflower = {
    'name': 'starflower',
	'desc': 'The mythical starflower. Legend says that _____...',
	'getable': True,
	'edible': False,
	'usable': False,
	'health': 'N/A',
	'inv': 0
	}

#This is a list of usable items:
flower = {
    'name': 'flower',
	'desc': '''Although it might look shabby, this particular flower (flax flower)
can be used to make string, which is used in multiple different tools
(see help).''',
    'getable': True,
	'edible': False,
	'usable': True,
	'health': 'N/A',
	'string': 'You use the flower to make string(1)',
	'getitem': string,
	'usenumber': 1,
	'inv': 0
	}
flower1 = copy.copy(flower)
flower2 = copy.copy(flower)
flower3 = copy.copy(flower)
flower4 = copy.copy(flower)
flower5 = copy.copy(flower)

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

fish = {
    'name': 'fish',
	'desc': 'A fresh fish. You\'ll need to cook it before eating it.',
	'getable': False,
	'edible': True,
	'usable': False,
	'health': 7,
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
    'usenumber': 4,
    'inv': 0
    }
rod = {
    'name': "rod",
	'desc': 'An old fishing rod. It seems to be holding up ok.',
	'getable': False,
	'edible': False,
	'usable': True,
	'health': 0,
	'ingredients': [stick, string, bone],
	'string': '''You cast the fishing rod into the water. but will it yield a fish?''',
	'getitem': fish,
	'usenumber': 6,
	'inv': 0
	}








