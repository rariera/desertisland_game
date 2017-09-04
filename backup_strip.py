from tkinter import *
import time
from PIL import Image, ImageTk
import sys
import textwrap
import collections
import random

#Ideas
    #Fishing spot
    #tools e.g. axe, fishing rod
    #Mini-locations - cmd.verb == 'enter'
    #
    

#Ask Dad:
    #Cloning coconuts - coconut(2)?
    
    


#Things to do:
    #Setting Descriptions - good and incorporate all items in list
    #Multiple instanses of the same object in an area, e.g. 2 coconuts - put in setting? 
    #Inventory and i['inv'] sync
    #Complete Mysterious Help Station
    #Make other settings


#Things that need altering for tkinter:
    #turn_no referenced before assignment
    #entryget() does not include prper commands - yay does not count!!!
    


class Character(object):
    def __init__(self, loc, health, inventory = []):
        self.loc = loc
        self.inventory = inventory
        self.health = health
        chooseroom(self)
        
def parsecommand(userinput):
    '''This is where i separates the command into the 'verb' (e.g. get), and the 'item' (e.g. coconut)'''
    ParsedCommand = collections.namedtuple('ParsedCommand', ['verb', 'item'])
    tokens = userinput.split(' ')
    verb = tokens.pop(0)
    if len(tokens) > 0:
        return ParsedCommand(verb, ' '.join(tokens))
    else:
        return ParsedCommand(verb, '')

def finditem(itemname, container):
    for i in container:
        if i['name'] == itemname:
            return i

def death():
    respawn = input('You died! Would you like to respawn? ')
    if respawn == 'yes':
        it = initialisation()
        global character
        character = it.character
        turn_no = it.turn_no
    else:
        exit()

def chooseroom(character):
    """This is where it decides where the character is."""
    if character.loc == [1,2]:
        character.room = beach
    elif character.loc == [1,1]:
        character.room = rocks
    elif character.loc == [2,2]:
        character.room = jungle
    elif character.loc == [2.5,2]:
        character.room = clearing
    elif character.loc == [3,2]:
        character.room = mountain
    else:
        write(text, 'I can\'t choose a room!!!')

def roomreset():
    beach['items'] = [coconut, rope, seagull]
    rocks['items'] = [rock, starfish, shellfish]


def get(item):
    if item not in character.inventory:
        character.inventory.append(item)
        item['inv'] = item['inv'] + 1
    else:
        item['inv'] = item['inv'] + 1

def invcheck():
    for item in character.inventory:
        if item['inv'] < 1:
            character.inventory.remove(item)

def clone(item):
    index = 1
    newitem = item.copy()
    write(text, newitem)
    return newitem

#--------------------------------------------------------------------------------#

def animation():
    if animation.index == -1:
        return
    imagecanvas = canvas.create_image(0, 0, anchor = NW, image = frames[animation.index])
    animation.index = animation.index + 1
    if animation.index > 3:
        animation.index = 0
    root.after(300, animation)

def delete(widget):
    widget.grid_forget()

def showimg():
    root.photo = photo
    imagecanvas = canvas.create_image(0,0, anchor = NW, image = photo)
    cont.configure(text = 'let\'s go!!', command = showoimg)
    animation.index = -1

def showoimg():
    animation.index = 0
    animation()
    root.photo = photo
    cont.configure(text = 'let\'s not?', command = showimg)



def write(textbox, string):
    textbox.delete('1.0', END)
    textbox.insert('end', string)
    

def entryget(Event = None):
    userinput = input.get()
    print(userinput)
    if userinput == 'yay':
        write(text, 'Yeah, that\'s it!')
    elif userinput == '':
        write(text, 'No, you need to type something in!')
    
root = Tk()
root.geometry('765x700')
root.configure(background = 'blue4')

welcome = Label(text = '''Welcome to Steve\'s game!\n
Type something in the entry\n
box to begin!''', bg = 'blue4', fg = 'white')
welcome.grid(row = 0, column = 0)

cont = Button(text = 'Continue?', command = showimg)
cont.grid(row = 0, column = 1)

text = Text(width = 70, height = 15)
text.grid(columnspan = 3, row = 3, column = 0)
text.insert('end', 'once upon a time....')

canvas = Canvas(width = 533, height = 535)
canvas.grid(rowspan = 3, columnspan = 3, row = 0, column = 2)
photo = ImageTk.PhotoImage(file = 'desert.png')
    
input = Entry()
input.grid(row = 1, column = 0)

userinput = ''

confirm = Button(text = 'Enter', command = entryget)
confirm.grid(row = 1, column = 1)

input.bind('<Return>', loop)



frames = [ PhotoImage(file='guy_horse.gif', format = 'gif -index %i' % i) for i in range(0,4) ]

animation.index = 0
animation()






##def itemcount(item):
##    count = character.room['items'].count(item)
##
##def roomcount():
##    numlist = []
##    for item in character.room['items']:
##        itemcount(item)
##        numlist.append()

#This will be the info about all the objects in the game.
coconut = {
    'name': 'coconut',
    'desc': "Here is a coconut",
    'getable': True,
    'edible': True,
    'usable': False,
    'health': 5,
    'inv': 0
        }
rope = {
    'name': 'rope',
    'desc': 'Here is a wet piece of rope. It must have washed up from your shipwreck.',
    'getable': True,
    'edible': False,
    'usable': True,
    'health': 0,
    'inv': 0
    }
seagull = {
    'name': 'seagull',
    'desc': '''A seagull swoops in the sky, searching for food. It eyes you in a way that
makes you feel uncomfortable...''',
    'getable': False,
    'edible': True,
    'usable': False,
    'health': 8,
    'inv': 0
    }
rock = {
    'name': 'rock',
    'desc': 'Here is a sharp piece of rock. Maybe you could use it to make something...',
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
    'desc': '''An old stick. You stare at it for a moment. You wonder about what it could have been, and
    what it may yet become.''',
    'getable': True,
    'edible': False,
    'usable': False,
    'health': 0,
    'inv': 0
    }
vine = {
    'name': 'vine',
    'desc': 'You pull on a vine. It comes off in your hand. Easy to break, but may still be useful...',
    'getable': True,
    'edible': False,
    'usable': False,
    'health': 0,
    'inv': 0
    }
berry = {
    'name': 'berry',
    'desc': """A purple berry. You roll it in your hand. It could be delicious, but what
    if it kills you instead?""",
    'getable': True,
    'edible': True,
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
    'string': 'You use the axe. The sapling falls to the ground, another defeated foe >:). You got 1 wood.',
    'getitem': wood,
    'settings': [5],
    'inv': 0
    }



itemslist = [coconut, rope, seagull, rock, starfish, shellfish, stick, vine, berry, wood, axe]
toolslist = [axe]

#This is the info about the rooms...
beach = {
    'locname': 'beach',
    'location': [1,2],
    'setting': """Around you are small yellow particles littering the beach. Oh wait, it\'s just sand.
    To the right is an impassable shelf of rock. In front of you is a small winding trail,
    leading into the jungle. To your left is more beach. And behind you?
    Behind you there is the endless ocean, the waves lapping at the shore, so reminisent
    of the storm that caused you to wash up on this desolate beach. To your left, a coconut tree sags""",
    'tools': [],
    'items': [coconut, rope, seagull]
    }

rocks = {
    'locname': 'rocks',
    'location': [1,1],
    'setting': '''Around you are many rocks: misshappen lumps of granite that long ago fell here in a
meteor shower. It seems many animals have made their home here: starfish, shellfish, in one of the
rock pools, you even see a tiny trout!''',
    'tools': [],
    'items': [rock, starfish, shellfish]
    }

jungle = {
    'locname': 'jungle',
    'location': [2,2],
    'setting': '''Around you vines hang low over the game trail, threatening to wrap you in their deadly
embrace. By the trail, there are many sticks that litter the ground, and a berry bush on your right.
Luckily, there is a clearing here that you should be able to Enter, to take shelter for the night.
the game trail continues to the east, west, and north.''',
    'tools': [axe],
    'items': [stick, vine, berry]
    }

clearing = {
    'locname': 'clearing',
    'location': [2.5,2],
    'setting': '''A soft clearing is spread out before you. The various trees around you branch together
like a low ceiling, sheltering you from the darkened skies. For the first time in a long while, you feel
safe.
This looks like a good place to make camp.''',
    'tools': [],
    'items': []
    }

mountain = {
    'locname': 'mountain',
    'location': [3,2],
    'setting': '''You find yourself at the foot of an impassable mountain. Around you, rocks litter the
    ground, threatening to trip you at every turn.  North of you, a cave leads downwards into darkness.
    To your ease, a short dirt path leads to a waterfall, overflowing into a mountain spring.''',
    'tools': [],
    'items': [rock]
    }

village = {
    'locname': 'village',
    'location': [2,1],
    'setting': '''Around you stands the ruins of an ancient village. The ground is dusty and dry beneath
your feet. You can see by the workmanship on the houses that this was once a society, filled with life
and purpose. However, it seems as though any life in this village has long since passed on. Now the
village stands desolate, alone on this dusty hillside. It suddenly hits you that perhaps
you won't make it home after all...
As you look about the dusty village, you begin to notice that many of the homes around here are in ruins,
worn away by the course of time. However, one house near the edge of the village seems mostly
intact. Perhaps you could enter here and take refuge?''',
    'tools': [],
    'items': []
    }

waterfall = {
    'locname': 'waterfall',
    'location': [3,3],
    'setting': '''Before you there is a waterfall, filled with crystal clear water rushing quickly into
the mountain spring at your feet. As it hits the surface of the water, it sends up white froth in all
directions. To your west, there is a short dirt path, leading back to the mountain. To the south lies
a grassy hillside, covered with wildflowers.
There are [items]''',
    'tools': [],
    'items': []
    }


rooms = [beach, rocks, jungle, clearing, mountain, village, waterfall]

def initialisation():

    write(text, """
    Welcome to the desert island game
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

    If you are unsure what to do, type 'help'.""")


    InitTuple = collections.namedtuple('InitTuple', ['character', 'turn_no'])
    character = Character(loc = [1,2], health = 20, inventory = [])
    print('initialisaton is awesome!')
    roomreset()
    global turn_no
    turn_no = 0
    return InitTuple(character, turn_no)



#Calling initialisation...
it = initialisation()
character = it.character
#turn_no = it.turn_no
global turn_no
print(str(turn_no))







#-------------------------------------------------------------------------------------------------------#
#This is where the loop begins...

def loop():
##    command = input("""What will you do?
##>>> """)
    cmd = parsecommand(userinput)
    print(cmd.verb)
    print(cmd.item)
    if cmd.item:
        if cmd.verb in ['get']:
            collection = character.room['items']
        elif cmd.verb in ['examine', 'ex', 'eat', 'use']:
            inventory_list = [i['name'] for i in character.inventory]
            if cmd.item in inventory_list:
                collection = character.inventory
            else:
                collection = character.room['items']
        else:
            collection = itemslist
        item = finditem(cmd.item, collection)
    else:
        item = 'null'
    
            
#This is all of the commands that can be used by the player

    if cmd.verb in ['help', 'h']:
        write(text, """You hear a mysterious voice coming from the nearest place of concealment.
It says: Hello! I am the Mysterious Help Station, or MHS for short.
I will aid you in your quest. Here is a list of commands you can use to survive in this world.
Use it well...

    look/l - Tells you what you can see.
    get _______ - Can be used to pick up an item - Note not all items are getable.
    inventory/i - Tells you what is in your inventory
    eat _______ - Can be used to eat an item - Note not all items are edible.
    health - Tells you how much health you have left
    help - I will come and aid you once more... if you say please...
    n, s, w, e - Used to move from place to place - Note you can only go in certain directions
                in each room, as indicated by the description.
    examine/ex - In some settings, there are mini-locations that you can enter - as indicated
    by the description
    enter/exit - can be used to enter or exit a mini-location inside a room, as indicated by description
    rest - used to restore 10 HP - can only be done inside safe location

If you need help on a specific topic, type 'topics' in the help prompt, and I will list the topics
I can assist you on. If you wish to leave the MHS, type 'leave' to exit the help station.

Please note, some commands are secret, and must be discovered for yourself.
Good luck, Traveller....
(The voice fades away)""")
        
        while True:
            helpcommand = input('help> ')
            helpcmd = parsecommand(helpcommand)

            if helpcmd.verb == 'leave':
                break
            
            elif helpcmd.verb in ['topics']:
                write(text, '''Topics I can tell you about are:
                              - game
                              - food
                              - crafting
                              - HP
                              - 
                        ''')
            elif helpcmd.verb == 'game':
                write(text, '''The desert island game is a game where you are trapped on a deserted island.
The aim of the game is to survive, and eventually make your escape.''')
            elif helpcmd.verb == 'food':
                write(text, '''Food can be used in the game to restore HP. It can be stored in the
inventory until time of consumption, at which point it will be removed from the inventory.''')
            elif helpcmd.verb == 'crafting':
                write(text, '''Crafting is where you combine multiple different items together into
a new item. This can be done using the 'make' command, written as 'make [item]', and if you have
all the neccasary items for the item, it will be created and put into your inventory. The items
used to make it will then be erased.''')
            elif helpcmd.verb in ['HP', 'hp', 'health']:
                write(text, '''Health points, or HP, is a way of measuring a characters health. If your HP
reaches 0, you will DIE!!!! In order to regain HP, you can eat food or rest in a safe place.
You will lose HP through battles, moving from place to place, and gradual starvation(1 HP every 5 turns)''')

                      
    elif cmd.verb in ['look', 'l']:
        write(text, character.room['setting'])
        
    elif cmd.verb == '_items':
        name_list = [i['name'] for i in character.room['items']]
        write(text, ', '.join(name_list))

    

    elif cmd.verb in ['get']:
        if cmd.item == 'trout' and character.room == rocks:
            write(text, 'You try to grab the trout.... But it eludes you, staring back in disdain.')
            write(text, 'If only you had something to catch it in...')
            #continue
        if cmd.item == 'seagull' and character.room == beach:
            write(text, 'You try to grab the seagull... but it poops on your head.')
            #continue
        if item in character.room['items'] and item['getable']and len(character.inventory) < 10:
            write(text, 'You picked up the ' + cmd.item)
            character.room['items'].remove(item)
            get(item)
        elif len(character.inventory) == 10:
            write(text, 'Sorry, your inventory is full. You cannot carry more than 10 items.')
        elif item not in character.room['items']:
            write(text, 'get... what? That ain\'t even in this place!')
        elif not item['getable']:
            write(text, 'You can\'t pick that up!')
        else:
            write(text, 'ERROR!!! REALITY DISSOLVING! TIMELINE RESETING! YOU DISCOVERED A BUG!!! AHHHHH!')
            death()


    elif cmd.verb in ['use', 'u']:
        if item in toolslist and character.inventory:
            if item in character.room['tools']:
                get(item['getitem'])
                write(text, item['string'])
        elif item in toolslist:
            write(text, 'You don\'t have one of those!')
        elif item in character.inventory:
            write(text, 'You can\'t use that!')
        else:
            write(text, 'What??? You can\'t use something you don\'t have which is not a tool!!! Dude....')
                
    elif cmd.verb in ['inventory', 'i']:
        if len(character.inventory) > 0:
            inventory_list = [i['name'] + '(' + str(i['inv']) + ')' for i in character.inventory]
            write(text, ', '.join(inventory_list))
        else:
            write(text, "You have nothing in your inventory... so sad.")
        #continue

    elif cmd.verb in ['eat']:
        if item == 'null':
            write(text, 'What do you want to eat?')
            #continue
        if item and item['edible'] and item in character.inventory:
            if character.health < 20:
                write(text, 'You eat the ' + cmd.item)
                if item == berry:
                    if random.randint(1,2) == 1:
                        berry['health'] = 10
                    else:
                        write(text, 'It seems the berry was poisoned! You lost 10 health points!')
                        berry['health'] = -10
                item['inv'] = item['inv'] - 1
                invcheck()
                character.health = character.health + item['health']
                if character.health > 20:
                    character.health = 20
                write(text, 'Your health level is now ' + str(character.health))
            else:
                write(text, 'You aren\'t in need of energy just now')
                #continue
        elif item not in character.inventory:
            write(text, 'You don\'t even have that, silly!')
        elif not item['edible']:
            write(text, 'You want to eat that? No. Just... no.')

    elif cmd.verb == 'health':
        write(text, 'You have ' + str(character.health) + '/20 HP.')
        #continue

    elif cmd.verb in ['west','w']:
        if character.loc[1] in [2]:
            write(text, 'You walk to the west.')
            character.loc[1] = character.loc[1] - 1
            chooseroom(character)
            write(text, 'You are now at the ' + character.room['locname'])
            write(text, character.room['setting'])
            character.health = character.health - 2
        else:
            write(text, 'You can\'t go that way!')
        
    elif cmd.verb in ['east','e']:
        if character.loc[0] in [1] and character.loc[1] in [1]:
            write(text, 'You walk to the east.')
            character.loc[1] = character.loc[1] + 1
            chooseroom(character)
            write(text, 'You are now at the ' + character.room['locname'])
            write(text, character.room['setting'])
            character.health = character.health - 2
        else:
              write(text, 'You can\'t go that way!')
              
    elif cmd.verb in ['north','n']:
        if character.loc[0] in [1,2] and character.loc[1] in [2,3]:
            write(text, 'You walk to the north.')
            character.loc[0] = character.loc[0] + 1
            chooseroom(character)
            write(text, 'You are now at the ' + character.room['locname'])
            write(text, character.room['setting'])
            character.health = character.health - 2
        else:
              write(text, 'You can\'t go that way!')
              
    elif cmd.verb in ['south','s']:
        if character.loc[0] in [3,2] and character.loc[1] in [2,3]:
            write(text, 'You walk to the south.')
            character.loc[0] = character.loc[0] - 1
            chooseroom(character)
            write(text, 'You are now at the ' + character.room['locname'])
            write(text, character.room['setting'])
            character.health = character.health - 2
        else:
              write(text, 'You can\'t go that way!')    


    elif cmd.verb in ['examine', 'ex']:
        write(text, 'This is the info on the ' + item['name'])
        write(text, 'Name: ' + item['name'])
        write(text, 'Description: ' + item['desc'])
        write(text, 'Getable: ' + str(item['getable']))
        write(text, 'Edible: ' + str(item['edible']))
        write(text, 'Usable: ' + str(item['usable']))
        write(text, 'HP avaliable: ' + str(item['health']))
 

    elif cmd.verb in ['enter']:
        if character.room in [jungle]:
            character.loc[0] = character.loc[0] + 0.5
            chooseroom(character)
            write(text, 'You enter the ' + character.room['locname'])

    elif cmd.verb in ['exit']:
        if character.room in [clearing]:
            write(text, 'You exit the ' + character.room['locname'])
            character.loc[0] = character.loc[0] - 0.5
            chooseroom(character)

    elif cmd.verb in ['rest', 'r']:
        if character.room in [clearing]:
            write(text, 'You lie down on the soft ground. You slowly drift into sleep...')
            write(text, 'Your HP increased by 10.')
            character.health = character.health + 10
            if character.health > 20:
                character.health = 20
        else:
            write(text, 'Dude, what kind of survivalist sleeps in a potentially hostile location???')

    elif cmd.verb == '_teleport':
        for i in rooms:
            if i['locname'] == cmd.item:
                write(text, 'Success! You have teleported to the ' + i['locname'])
                character.loc = i['location']
                chooseroom(character)

        
        
    elif cmd.verb == '_get':
        if item in itemslist:
            if len(character.inventory) > 10:
                write(text, '''Caution! Your inventory is less than 10! In order to \'get\' things, you will need to
                      keep your items under 10!''')
            get(item)
        else:
            write(text, 'not real, dude.')
            #continue

    
    elif cmd.verb == '_die':
        death()

    elif cmd.verb == '_five':
        character.health = character.health - 5


    
    else:
        write(text, '''I\'m sorry, but that is not a valid command. If you require assistance,
please consult the MHS by typing help''')
        #continue


    #This is turn-based health deductor
    if it.turn_no < 5:
        turn_no = it.turn_no + 1
    else:
        character.health = character.health - 1
        turn_no = 0

 

        
#Low health warning
    if character.health <= 5 and character.health >= 1:
        write(text, 'Caution! Your health is ' + str(character.health) + '''/20! if you do not
regain health soon, you will DIE!!!''')
    else:
        write(text, 'You have ' + str(character.health) + '/20 HP.')
#Death by starvation
    if character.health <= 0:
        write(text, '''You stumble a few paces. You slowly sway, and then fall into the dirt,
utterly exhausted. You do not move again...''')
        death()

    print('END OF LOOP!')



print('the test is complete')
root.mainloop()
