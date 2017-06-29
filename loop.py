import check_command
import rooms
from items import *
import gfunctions
import cfunctions
import health
from tkinter import *
from tkintermaker import *
from gfunctions import parsecommand

itemslist = [coconut, rope, seagull, rock, starfish, shellfish, stick, vine, berry, wood, axe]

def entryget(Event = None):
	global userinput
	userinput = entry.get()
	print("inputsssss")
	print(userinput)
	if userinput == 'yay':
		write(text, 'Yeah, that\'s it!')
	elif userinput == '':
		write(text, 'No, you need to type something in!')

global turn_no
turn_no = 0

def loop(self):
    entryget()
    cmd = parsecommand(userinput)
    collection = itemslist
    item = gfunctions.finditem(cmd.item, collection)

    check_command.check_command(cmd, item)
    check_command.chealth_check(turn_no)
    check_command.chealth_warning()
    check_command.cstarvation_check()

entry = Entry()
entry.grid(row = 1, column = 0)



confirm = Button(text = 'Enter', command = loop)
confirm.grid(row = 1, column = 1)





    

    
    
    
    
    
    
