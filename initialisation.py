import tkintermaker
import collections
from classes import Output
from gfunctions import roomreset


write = Output.write

def initialisation():
    write(tkintermaker.text, '''Welcome to the desert island game
Are you ready??
You slowly awaken to a dazzling bright light.
It's the sun.
Aduh!
Haven't you played these games before?
Point is you’re stuck on a desert island.
The smell of salt is on the air.
Above you, seagulls circle in the sky like vultures,
looking for their next meal... Yeah, you should
probably get away from here
You see a shelf of rock to the east,
To the west, the beach stretches out of sight.
The jungle is to the north of you and the ocean the south.
The sun blazes on above you.
If you are unsure what to do, type 'help'.''')


    InitTuple = collections.namedtuple('InitTuple', ['turn_no'])
    tkintermaker.much('beach1')
    print('initialisation has completed')
    roomreset()
    global turn_no
    turn_no = 0
    return InitTuple(turn_no)