import check_command

from items import *
from tkinter import *
from tkintermaker import *
from gfunctions import parsecommand, finditem

itemslist = [coconut, rope, seagull, rock, starfish, shellfish, stick, vine, berry, book, string, starflower, bone, flower, fish, wood, axe, rod, steel, flint, pickaxe]
toolslist = [axe, rod, flower, flint, pickaxe]
makelist = [axe, rod, flint, pickaxe]


def entryget(Event = None): 
	global userinput
	userinput = entry.get()
	entry.delete(0,'end')

global turn_no
turn_no = 0

def dispinv():
    check_command.dispinvent()

def dispcred():
    check_command.credits()
    
def disphelpb():
    check_command.disphelp()

def dispcraft():
    check_command.crafting()

def exitbutton():
    check_command.exithelp()
    
def lookbutton():
    check_command.lookie()

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
credits.grid(column = 4, row = 5)

helpbutton = Button(text = 'Help', command = disphelpb)
helpbutton.grid(column = 3, row = 3)

craftbutton = Button(text = 'Crafting', command = dispcraft)
craftbutton.grid(column = 3, row = 5)

exitbutton = Button(text = 'Exit Help', command = exitbutton)
exitbutton.grid(column = 4, row = 3)

lookbutton = Button(text = 'Look', command = lookbutton)
lookbutton.grid(column = 4, row = 4)



    

    
    
    
    
    
    
