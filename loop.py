import check_command

from items import *
from tkinter import *
from tkintermaker import *
from gfunctions import parsecommand, finditem

itemslist = [coconut, rope, seagull, rock, starfish, shellfish, stick, vine, berry, book, string, starflower, bone, flower, fish, wood, axe, rod, steel, flint]
toolslist = [axe, rod, flower, flint]
makelist = [axe, rod, flint]


def entryget(Event = None): 
	global userinput
	userinput = entry.get()
	entry.delete(0,'end')
	print(userinput)

global turn_no
turn_no = 0

def dispinv():
    check_command.dispinvent()

def dispcred():
    check_command.credits()

def loop(self):
    entryget()
    cmd = parsecommand(userinput)
    collection = itemslist
    item = finditem(cmd.item, collection)
    

    check_command.check_command(cmd, item, collection, toolslist, makelist)
    check_command.chealth_check(turn_no)
    check_command.chealth_warning()
    check_command.cstarvation_check()

entry = Entry()
entry.grid(row = 1, column = 0)

invent = Button(text = 'Inventory', command = dispinv)
invent.grid(column = 3, row = 4)

credits = Button(text = 'Credits', command = dispcred)
credits.grid(column = 3, row = 3)

confirm = Button(text = 'Enter', command = loop)
confirm.grid(row = 1, column = 1)





    

    
    
    
    
    
    
