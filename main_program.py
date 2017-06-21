#Coconut make a class!!! then can make instances of class (see ex.41, Learn python the hard way)

from tkinter import *
import time
from PIL import Image, ImageTk
import sys
import textwrap
import collections
import random

import rooms
from items import *
import gfunctions
import tfunctions
import cfunctions
from tkintermaker import *
from initalisation import *
import check_command
import health
import loop

class Character(object):
    def __init__(self, loc, health, inventory = []):
        self.loc = loc
        self.inventory = inventory
        self.health = health
        chooseroom(self)

itemslist = [coconut, rope, seagull, rock, starfish, shellfish, stick, vine, berry, wood, axe]
toolslist = [axe]
tkintermake()


#Calling initialisation...
it = initialisation()
character = it.character
#turn_no = it.turn_no
global turn_no
print(str(turn_no))



print('the test is complete')
root.mainloop()



