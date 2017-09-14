from items import *

#This is the info about the rooms...
beach1 = {
    'locname': 'beach',
    'location': [1,2],
    'setting': """Around you are small yellow particles littering the beach. Oh wait,
it\'s just sand. To the east is an impassable shelf of rock. In
front of you is a small winding trail, leading into the jungle.
To your west is more beach, leading down to a rocky inlet. And 
behind you? Behind you there is the endless ocean, the waves 
lapping at the shore, so reminisent of the storm that caused 
you to wash up on this desolate beach. To your left, a coconut
tree sags, offering you it's fruit. There is also a piece of 
rope here.

[You can go north or west]
""",
    'tools': [flint],
    'items': [coconut1, coconut2, coconut3, rope1, seagull1],
    'fire': False,
    'background': 'beach.png',
    'music': 'ocean.wav'
    }

rocks1 = {
    'locname': 'rocks',
    'location': [1,1],
    'setting': '''Around you are many rocks: misshappen lumps of granite that long ago
fell here in a meteor shower. It seems many animals have made their
home here: starfish, shellfish, in one of the rock pools, you even 
see a cute lil' trout!
[you can go fishing here with a rod]
The trail continues to the east.''',
    'tools': [rod, pickaxe],
    'items': [rock4, rock5, starfish, shellfish],
    'background': 'rocks.png',
    'music': 'ocean.wav'
    }

jungle1 = {
    'locname': 'jungle',
    'location': [2,2],
    'setting': '''Around you vines hang low over the game trail, threatening to wrap you
in their deadly embrace. By the trail, there are many sticks that
litter the ground, and a berry bush on your right. Luckily, there
is a clearing here that you should be able to Enter, to take shelter
for the night. The game trail continues to the south, west, and north.
[You can use an axe here to get wood.]''',
    'tools': [axe],
    'items': [stick1, stick2, vine1, vine2, berry1, berry2, berry3, berry4],
    'background': 'jungle.png',
    'music': 'danger.wav'
    }

clearing1 = {
    'locname': 'clearing  ',
    'location': [2.5,2],
    'setting': '''A soft clearing is spread out before you. The various trees around you
branch together like a low ceiling, sheltering you from the darkened
skies. For the first time in a long while, you feel safe.
This looks like a good place to make camp.
[You can rest here, and leave the clearing with 'exit'.]''',
    'tools': [],
    'items': [],
    'background': 'clearing.png',
    'music': 'clearing.wav'
    }

mountain1 = {
    'locname': 'mountain',
    'location': [3,2],
    'setting': '''You find yourself at the foot of an impassable mountain. Around you,
rocks litter the ground, threatening to trip you at every turn.
To your ease, a short dirt path leads to a waterfall, overflowing
into a mountain spring.
From here, one can see over the dense vegetation of the jungle,
showing the island in its' entirety. You feel very powerful, like
the ruler of a kingdom, albiet a very sad one, as you have no people
to rule over. :(
After all, this IS a deserted island.
A little ahead, you spot a mountain goat doing whatever mountain
goats do.
It looks a bit hungry though... [try and feed goat with 'use ____']
There is a pile of rocks here.
[You can use a pickaxe here, to get steel. The trail continues to the
south and east.]''',
    'tools': [pickaxe, starflower],
    'items': [rock1, rock2, rock3, coconut],
    'background': 'mountains.png',
    'music': 'wind.wav'
    }

village1 = {
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
intact. Perhaps you could Enter here and take refuge?
[The trail continues into the jungle, to the east.']''',
    'tools': [],
    'items': [],
    'background': 'village.png',
    'music': 'abandoned.wav'
    }

house1 = {
    'locname': 'house',
	'location': [2.5,1],
	'setting': '''You open the door and look around, amazed by what you see. 
Old, broken chairs and tables sit in front of you, a rickety bed in 
the corner, and against the back wall is a bookshelf. 
Despite this being the strongest building in the village, it is still
barely holding together. Wind whistles through cracks in the
walls, and the roof sags so much that the door refuses to stay
closed. But then again, the floor is soft, and in here, you can
relax. There is a rod, an old book and some bones here.
[you can rest here. To leave, type 'exit']''',
    'tools': [],
	'items': [rod, book, bone1, bone2, bone3],
    'background': 'house.png',
    'music': 'haven.wav'
	}
	


waterfall1 = {
    'locname': 'waterfall',
    'location': [3,3],
    'setting': '''Before you there is a waterfall, filled with crystal clear water
rushing quickly into the mountain spring at your feet. As it hits the
surface of the water, it sends up white froth in all directions. A
long vine hangs down, begging for you to grasp it and jump in to the
cool, refreshing water. To your west, there is a short dirt path, 
leading back to the mountain. To the south lies a grassy hillside, 
covered with wildflowers.
[You can fish here with a rod. The trail continues to the west and south.]''',
    'tools': [rod],
    'items': [vine3],
    'background': 'waterfall.png',
    'music': 'waterfall.wav'
    }

hill1 = {
    'locname': 'hill',
	'location': [2,3],
	'setting': '''You stand on a grassy hillside, surrounded by flowers. The wind
whistles through the grass, causing it to roll in waves around you.
to the south of you lies a path uphill leading to a cliff, to the 
north of you lies the waterfall.
[You can go to the north, or south]''',
	'tools': [],
	'items': [flower1, flower2, flower3, flower4, flower5, rock1],
        'background': 'hill.png',
        'music': 'hills.wav'
	}

cliff1 = {
    'locname': 'cliff',
	'location': [1,3],
	'setting': '''You stand on the edge of a cliff, a rocky precipice leading downward
onto the unforgiving rocks below. Looking to your right, far below
you lies the beach where you washed up. You feel amused as you
realise there is still a life sized intentation in the sand.

Just before the edge of the cliff lies a silver flower, a starflower,
glistening in the sun. You can tell there is something very special
about this flower.
[The trail continues to the north]''',
	'tools': [pickaxe],
	'items': [starflower],
    'background': 'cliff.png',
    'music': 'wind.wav'
	}

cave1 = {
    'locname': 'cave',
	'location': [3.5,3],
	'setting': '''You enter into a world of water and magical glowy things. What a good 
cave! You walk further into the cave, leaving the waterfall behind
you. Seeing a small hole in the rock, you bend down and crawl through
Before you there is a large round room, illuminated by a faint blue
light eminating from the many plants in the room.
You walk towards one of them, a large glowing blue mushroom.
'I wouldn't touch that if I were you.' A familiar voice says behind
you.
You whirl around, but there is no one there...?
'Over here.' You turn back towards the mushroom. A strange man stands
before you.
'Who are you?' You ask, trying and failing to sound unafraid. Despite
this, you hear your voice tremble.
'My name is Matthew Henry Scott. You may know me as... the MHS.
You need not be afraid, I am not going to harm you.

I waited for you here, to find out if you are worthy, but now, weary
traveller, I can bestow upon you the secrets of the island.
These are known as the secret commands, which will give you ultimate
power on the island.
They can be accessed in the help menu (MHS) by typing the keyword
'secret'
Just to repeat, these can be accessed in help by typing 'secret'

Now, follow me. I shall provide you safe passage...
[press Enter]
''',
	'tools': [],
	'items': [rock, book],
    'background': 'cave.png',
    'music': 'cave.wav'
}
roomslist = [beach1, rocks1, jungle1, clearing1, mountain1, village1, house1, waterfall1, hill1, cliff1, cave1]
