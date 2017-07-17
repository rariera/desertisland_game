from items import *

#This is the info about the rooms...
beach = {
    'locname': 'beach',
    'location': [1,2],
    'setting': """Around you are small yellow particles littering the beach. Oh wait,
it\'s just sand. To the right is an impassable shelf of rock. In
front of you is a small winding trail, leading into the jungle.
To your left is more beach. And behind you? Behind you there is
the endless ocean, the waves lapping at the shore, so reminisent
of the storm that caused you to wash up on this desolate
beach. To your left, a coconut tree sags""",
    'tools': [],
    'items': [coconut, rope, seagull]
    }

rocks = {
    'locname': 'rocks',
    'location': [1,1],
    'setting': '''Around you are many rocks: misshappen lumps of granite that long ago
fell here in a meteor shower. It seems many animals have made their
home here: starfish, shellfish, in one of the rock pools, you even 
see a tiny trout!''',
    'tools': [],
    'items': [rock, starfish, shellfish]
    }

jungle = {
    'locname': 'jungle',
    'location': [2,2],
    'setting': '''Around you vines hang low over the game trail, threatening to wrap you
in their deadly embrace. By the trail, there are many sticks that
litter the ground, and a berry bush on your right. Luckily, there
is a clearing here that you should be able to Enter, to take shelter
for the night. The game trail continues to the east, west, and north.''',
    'tools': [axe],
    'items': [stick, vine, berry]
    }

clearing = {
    'locname': 'clearing',
    'location': [2.5,2],
    'setting': '''A soft clearing is spread out before you. The various trees around you
branch together like a low ceiling, sheltering you from the darkened
skies. For the first time in a long while, you feel safe.
This looks like a good place to make camp.''',
    'tools': [],
    'items': []
    }

mountain = {
    'locname': 'mountain',
    'location': [3,2],
    'setting': '''You find yourself at the foot of an impassable mountain. Around you,
rocks litter the ground, threatening to trip you at every turn. North
of you, a cave leads downwards into darkness. To your ease, a short 
dirt path leads to a waterfall, overflowing into a mountain spring.''',
    'tools': [],
    'items': [rock]
    }

village = {
    'locname': 'village',
    'location': [2,1],
    'setting': '''Around you stands the ruins of an ancient village. The ground is dusty
and dry beneath your feet. You can see by the workmanship on the
houses that this was once a society, filled with life and purpose.
However, it seems as though any life in this village has long since
passed on. Now the village stands desolate, alone on this dusty 
hillside. It suddenly hits you that perhaps you won't make it 
home after all...
As you look about the dusty village, you begin to notice that many
of the homes around here are in ruins, worn away by the course of
time. However, one house near the edge of the village seems mostly
intact. Perhaps you could enter here and take refuge?''',
    'tools': [],
    'items': []
    }

shack = {
    'locname': 'shack',
	'location': [2.5,1],
	'setting': '''Despite this being the strongest building in the village, it is still
barely holding together. Wind whistles through cracks in the
walls, and the roof sags so much that the door refuses to stay
closed. But then again, the floor is soft, and in here, you can
relax.
[you can rest here]''',
    'tools': [],
	'items': [rod, book]
	}
	


waterfall = {
    'locname': 'waterfall',
    'location': [3,3],
    'setting': '''Before you there is a waterfall, filled with crystal clear water
rushing quickly into the mountain spring at your feet. As it hits the
surface of the water, it sends up white froth in all directions. To
your west, there is a short dirt path, leading back to the mountain.
To the south lies a grassy hillside, covered with wildflowers.
There are [items]''',
    'tools': [rod],
    'items': []
    }

hill = {
    'locname': 'hill',
	'location': [3,2],
	'setting': 'to be completed',
	'tools': [],
	'items': [flower]
	}

cliff = {
    'locname': 'cliff',
	'location': [1,3],
	'setting': 'to be completed',
	'tools': [],
	'items': []
	}

roomslist = [beach, rocks, jungle, clearing, mountain, village, shack, waterfall, hill, cliff]
