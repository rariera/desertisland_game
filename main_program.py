#Coconut make a class!!! then can make instances of class (see ex.41, Learn python the hard way)

#from tkinter import *
#import time
#from PIL import Image, ImageTk
#import sys
#import textwrap
#import collections
#import random

#import rooms
from items import *
#import gfunctions
#import tfunctions
#import cfunctions
from tkintermaker import *
from initalisation import *
#import check_command
#import health
#import loop
from loop import entry, loop

entry.bind('<Return>', loop)



toolslist = [axe]
tkintermake()

#Calling initialisation...  
it = initialisation()
#character = it.character
turn_no = it.turn_no


root.configure(background = 'blue4')
print('the test is complete')
root.mainloop()



