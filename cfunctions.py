from rooms import *
import items
from classes import Output
from initialisation import initialisation
import tkintermaker
from tkintermaker import bach, much, shoeimg
from gfunctions import chooseroom, get, invcheck, roomreset
import random


write = Output.write
noreplace_write = Output.noreplace_write
#Pass in character in the brackets!!!!!
text = tkintermaker.text

def help_command(character):
    character.status = 'help'
    write(text, """You hear a mysterious voice coming from the nearest place of
concealment. It says: Hello! I am the Mysterious Help Station,
or MHS for short. I will aid you in your quest. Here is a list of
commands you can use to survive in this world.
Use it well...

look/l - Tells you what you can see.
get _______ - Can be used to pick up an item - Note not all items are
getable.
inventory/i - Tells you what is in your inventory
eat _______ - Can be used to eat an item - Note not all items are
edible.
health - Tells you how much health you have left
help - I will come and aid you once more... if you say please...
n, s, w, e - Used to move from place to place - Note you can only 
move in certain directions in each room, as indicated by the 
description
examine/ex _______ - In some settings, there are mini-locations that
you can enter - as indicated by the description
enter/exit - can be used to enter or exit a mini-location inside a
room, as indicated by description
rest - used to restore 10 HP - can only be done inside safe location
drop ____ - used to drop an item in your inventory

If you need help on a specific topic, type 'topics' in the help 
prompt, and I will list the topics I can assist you on.

IF YOU WISH TO LEAVE THE MHS, TYPE 'leave' TO EXIT THE HELP MENU.

Please note, some commands are secret, and must be discovered for 
yourself.
Good luck, Traveller....
(The voice fades away)""")

def leave_command(character):
    character.status = 'alive'
    write(text, 'You are now leaving the MHS. What do you do?')


def topics_command():
    write(text, '''Topics I can tell you about are:
                  - game
                  - food
                  - crafting
                  - HP/health
                  - 
                  (to leave the MHS, type 'leave')
            ''')
            

def game_command():
    write(text, '''The desert island game is a game where you are trapped on a deserted
island. The aim of the game is to survive, and eventually make your
escape.

(to leave the MHS, type 'leave'.)''')

def food_command():
    write(text, '''Food can be used in the game to restore HP. It can be stored in the
inventory until time of consumption, at which point it will be 
removed from the inventory.

(to leave the MHS, type 'leave'.)''')

def crafting_command(character):
    write(text, '''Crafting is where you combine multiple different items together into
a new item. This can be done using the 'make' command, written as 
'make [item]', and if you have all the neccasary items for the item,
it will be created and put into your inventory. The items used to 
make it will then be erased.
Items which can be made include:

Axe - rock, vine, stick
Pickaxe - rock, vine, stick
Rod - stick, string, bone
Flint - rock, steel

Hint: You can get string for making a rod by using a flower...
You can examine the items to learn more ('ex ____')
''')
    if character.status == 'help':
        noreplace_write(text, '(to leave the MHS, type \'leave\'.)')

def hpinfo_command():
    write(text, '''Health points, or HP, is a way of measuring a characters health. If
your HP reaches 0, you will DIE!!!! In order to regain HP, you can
eat food or rest in a safe place. You will lose HP through moving
from place to place and gradual starvation(1 HP every 5 turns)

(to leave the MHS, type 'leave'.)''')

def secret_command():
    write(text, '''*sigh* here are the secret commands again:
_get - used to instantly get any item in the game
_teleport - used to instantly teleport to any location in the game
_five - used to lose 5 health points (if you really want to...)
_die - if you want to die...?
_end1 - instantly takes you to the normal ending
_end2 - instantly takes you to the secret cave ending

(to leave the MHS, type 'leave'.)''')

def help_error():
    write(text, '''That is not something I know. pls type topics to find out what I can
tell you.

(to leave the MHS, type 'leave'.)''')

def look_command(character):
    write(text, character.room['setting'])
    
def items_command(room):
    ''' Returns a string listing the items in a room '''
    name_list = [i['name'] for i in room['items']]
    return ', '.join(name_list)

def get_command(cmd, character, item):
    if cmd.item == 'trout' and character.room == rocks1:
        write(text, '''You try to grab the trout.... But it eludes you, staring back in 
disdain.''')
        noreplace_write(text, '''If only you had something to catch it in...
[See crafting button for more info]''')
        #continue
    elif cmd.item == 'seagull' and character.room == beach1:
        write(text, 'You try to grab the seagull... but it poops on your head.')
        #continue
    elif cmd.item == 'goat' and character.room == mountain1:
        write(text, 'No, you cannot get the goat!')
    elif item in character.room['items'] and item['getable'] and len(character.inventory) < 10:
        write(text, 'You picked up the ' + cmd.item + '''. 
You can examine it using 'ex ____' or 'examine____'.''')
        if item['name'] == 'book':
            noreplace_write(text, '''(You can read the book by typing 'ex')''')
        elif item['name'] == 'flower':
            noreplace_write(text, '''You can Use a flower to make string''')    
        character.room['items'].remove(item)
        get(item, character)
        if item['edible']:
            noreplace_write(text, '''
Looks tasty....''')
    elif len(character.inventory) == 10:
        write(text, '''Sorry, your inventory is full. You cannot carry more than 10 items.
perhaps you could drop something to make room?''')
    elif item not in character.room['items']:
        write(text, 'get... what? That ain\'t even in this place!')
    elif not item['getable']:
        write(text, 'You can\'t pick that up!')


def use_command(character, item, toolslist):
    if item in character.inventory and item['usable']:
        if item in character.room['tools'] or item == flower:
            if item == rod:
                if random.randint(0,2) != 1:
                    write(text, item['string'])
                    get(item['getitem'], character)
                    noreplace_write(text, 'Success! You caught a fish!')
                else:
                    write(text, item['string'])
                    noreplace_write(text, 'You didn\'t catch a fish. Better luck next time!')
            elif item == starflower:
                character.inventory.remove(item)
                write(text, '''The goat slowly approaches you, eyeing the starflower in your hand.
Being the kind person that you are, you offer the goat your flower
and it quickly gobbles it up. The goat looks at you, its eyes
twinkling with years of wisdom, and speaks.
 
Where water doth lie 
And crickets do buzz 
There you will find a great secret 
Every hunter has seeked it, but 
Ruthless in his ways 
Failed to learn of the Entrance 
All clues doth lead to it 
Letters tumbling down
Leaving you with a message' it says. 

Enlightened by the goat's words, you continue on your journey...''')
            elif item['name'] == 'flint':
                wood = False
                for i in character.inventory:
                    if i['name'] == 'wood':
                        wood = True
                        woodremove = False
                        for i in character.inventory:
                            if woodremove == False:
                                if i['name'] == 'wood':
                                    character.inventory.remove(i)
                                    woodremove = True
                        if woodremove == True:
                            write(text, item['string'])
                            end1_command(character)
                            character.status = 'end1'
                if wood == False:
                    write(text, 'You need wood to make a fire!')
                    pass
            else:
                get(item['getitem'], character)
                write(text, item['string'])
            item['usenumber'] = item['usenumber'] - 1
            if item['usenumber'] < 1:
                character.inventory.remove(item)
                noreplace_write(text, 'Your ' + item['name'] + ' broke. Guess you ran out of uses.')
        else:
            write(text, 'You can\'t use that in this room.')
    elif item['edible'] and character.room == mountain1:
        write(text, '''The goat doesn't seem to like it... Maybe try something else?
(Hint: Try examining your items)''')
    elif item in toolslist:
        write(text, 'You don\'t have one of those!')
    elif item in character.inventory:
        write(text, 'You can\'t use that!')
    else:
        write(text, 'What??? You can\'t use something you don\'t have which is not a tool!!')
            
def inventory_command(character):
    quirk = False
    if len(character.inventory) > 0:
        namelist = {}
        stringlist = []
        for i in character.inventory:
            if i in stringlist:
                namelist[i['name']] = namelist[i['name']] + 1
            else:
                namelist[i['name']] = 1
                stringlist.append(i)
        inventory_list = [n + '(' + str(namelist[n]) + ')' for n in namelist]
        write(text, ', '.join(inventory_list))
    else:
        write(text, "You have nothing in your inventory... so sad.")

def eat_command(cmd, character, item):
    if item == 'null':
        write(text, 'What do you want to eat?') 
    elif item and item['edible'] and item in character.inventory:
        if character.health < 20:
            write(text, 'You eat the ' + cmd.item)
            if item == items.berry:
                if random.randint(1,2) == 1:
                    berry['health'] = 10
                else:
                    write(text, 'It seems the berry was poisoned! You lost 10 health points!')
                    berry['health'] = -10
            for i in character.inventory:
                if i['name'] == item['name']:
                    character.inventory.remove(i)
                    pass
            character.health = character.health + item['health']
            if character.health > 20:
                character.health = 20
            noreplace_write(text, 'Your health level is now ' + str(character.health) + '/20')
            noreplace_write(text, 'You gained ' + str(item['health']) + 'HP.')
        else:
            write(text, 'You aren\'t in need of energy just now')
            #continue
    elif item not in character.inventory:
        write(text, 'You don\'t even have that, silly!')
    elif not item['edible']:
        write(text, 'You want to eat that? No. Just... no.')

def health_command(character):
    write(text, 'You have ' + str(character.health) + '/20 HP.')
    #continue

def west_command(character):
    if character.room in [waterfall1, jungle1, beach1]:
        write(text, 'You walk to the west.')
        character.loc[1] = character.loc[1] - 1
        chooseroom(character)
        bach(character)
        much(character)
        noreplace_write(text, 'You are now at the ' + character.room['locname'])
        noreplace_write(text, character.room['setting'])
        character.health = character.health - 2
    else:
        write(text, 'You can\'t go that way!')
    
def east_command(character):
    if character.room in [mountain1, village1, rocks1]:
        write(text, 'You walk to the east.')
        character.loc[1] = character.loc[1] + 1
        chooseroom(character)
        bach(character)
        much(character)
        noreplace_write(text, 'You are now at the ' + character.room['locname'])
        noreplace_write(text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(text, 'You can\'t go that way!')
          
def north_command(character):
    if character.room in [beach1, jungle1, hill1, cliff1]:
        write(text, 'You walk to the north.')
        character.loc[0] = character.loc[0] + 1
        chooseroom(character)
        bach(character)
        much(character)
        noreplace_write(text, 'You are now at the ' + character.room['locname'])
        noreplace_write(text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(text, 'You can\'t go that way!')
          
def south_command(character):
    if character.room in [mountain1, waterfall1, jungle1, hill1]:
        write(text, 'You walk to the south.')
        character.loc[0] = character.loc[0] - 1
        chooseroom(character)
        bach(character)
        much(character)
        noreplace_write(text, 'You are now at the ' + character.room['locname'])
        noreplace_write(text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(text, 'You can\'t go that way!')    


def examine_command(item, cmd):
    if cmd.item == 'waterfall':
        noreplace_write(text, '''You look deeply at the waterfall. Seems like there is something - 
behind it?''')
    else:
        write(text, 'This is the info on the ' + item['name'])
        noreplace_write(text, 'Name: ' + item['name'])
        noreplace_write(text, 'Description: ' + item['desc'])
        noreplace_write(text, 'Getable: ' + str(item['getable']))
        noreplace_write(text, 'Edible: ' + str(item['edible']))
        noreplace_write(text, 'Usable: ' + str(item['usable']))
        if item['name'] in ['rod', 'pickaxe', 'axe', 'flint']:
            namelist = [i['name'] for i in item['ingredients']]
            noreplace_write(text, 'Ingredients:' + str(namelist))
        else:
            noreplace_write(text, 'Ingredients: N/A')
        noreplace_write(text, 'HP available: ' + str(item['health']))


def enter_command(character):
    if character.room in [jungle1, village1, waterfall1]:
        character.loc[0] = character.loc[0] + 0.5
        chooseroom(character)
        if character.room == cave1:
            write(text, 'You step through the waterfall....')
        else:
            write(text, '')
        bach(character)
        much(character)
        noreplace_write(text, 'You enter the ' + character.room['locname'])
        noreplace_write(text, character.room['setting'])
        if character.room == cave1:
            character.status = 'end2'

def exit_command(character):
    if character.room in [clearing1, house1, cave1]:
        write(text, 'You exit the ' + character.room['locname'])
        character.loc[0] = character.loc[0] - 0.5
        chooseroom(character)
        bach(character)
        much(character)
        noreplace_write(text, character.room['setting'])

def rest_command(character):
    if character.room in [clearing1, house1]:
        write(text, 'You lie down on the soft ground. You slowly drift into sleep...')
        noreplace_write(text, 'Your HP increased by 10.')
        noreplace_write(text, 'You wake up. What do you do now?')
        character.health = character.health + 10
        if character.health > 20:
            character.health = 20
    else:
        write(text, '''Dude, what kind of survivalist sleeps in a potentially hostile 
location???''')

def teleport_command(character, cmd):
    for i in roomslist:
        if i['locname'] == cmd.item:
            write(text, 'Success! You have teleported to the ' + i['locname'])
            character.loc = i['location']
            chooseroom(character)
            bach(character)
            much(character)

def make_command(item, character, makelist):
    if item in makelist:
        for i in item['ingredients']:
            if i in character.inventory:
                check = True
            else:
                write(text, 'You don\'t have all the ingredients')
                check = False
        if check == True:
            for i in item['ingredients']:
                character.inventory.remove(i)
            get(item, character)
            write(text, 'You made an ' + item['name'] + '. Check it out with \'ex\'')
            if item == flint:
                noreplace_write(text, '''Now all I need to make a fire is some wood! Now where can I find an
axe...''')
    else:
        write(text, 'You can\'t make that...')


def cget_command(character, item, collection):
    if item in collection:
        if len(character.inventory) > 10:
            write(text, '''Caution! Your inventory is less than 10! In order to \'get\' things,
you will need to keep your items under 10!''')
        get(item, character)
        write(text, 'Tada!! The ' + item['name'] + ' magically appeared in your inventory!!!')
    else:
        write(text, 'not real, dude.')
        


def die_command(character):
    death(character)
    character.health = 0

def five_command(character):
    character.health = character.health - 5
    write(text, 'You lost 5 HP.')

def drop_command(character, item):
    write(text, 'You drop the ' + item['name'] + '.')
    forloop = True
    for i in character.inventory:
        if i['name'] == item['name'] and forloop == True:
            character.inventory.remove(i)
            character.room['items'].append(i)
            forloop = False




def error_command():
    write(text, '''I\'m sorry, but that is not a valid command. If you require assistance,
please consult the MHS by typing help''')

def read_command():
	if character.room in [cave1]:
		write(text, 'Name: ' + item['name'])



def death(character):
    noreplace_write(text, 'You died. Would you like to respawn? (yes/no)')
    character.room = beach1
    character.inventory = []
    roomreset()
    character.health = -5
    character.status = False
    
def end1_command(character):
    shoeimg()
    write(text, '''
Your fire burns higher and higher. Huge columns of smoke begin to
billow into the sky. You scan the horizon, hoping to see some kind of
ship or aircraft, but to no avail.
Just as you're about to give up, far on the horizon, you see a low
cloud. No, it can't be a cloud, it's moving, moving this way. You 
feel a sense of triumph as you realise it's a red rescue helicopter.
It lands, and invites you aboard.

Congratulations! You successfully made your escape from the
deserted island in ''' + str(character.token + 1) + ''' turns!
But, there's another, secret ending you have yet
to discover. Do you want to continue playing? (yes/no)''')

def continue_command(character):
    write(text, '''Ok. Here's a secret clue that you might need to help things along.
Be nice to goats. They're smarter than you think.

Now, continue playing. I was never here....

Oh, also, when you're done playing, you can just gather some more 
wood and use the flint to call the helicopter again. See ya soon!
''')
    noreplace_write(text, character.room['setting'])
    
def continue2_command(character):
    write(text, '''Ok. I'll just drop you off at the waterfall. Hey, why don't
you head over to the village? Maybe that'll help you out. Bye!''')
    character.loc = [3,3]
    chooseroom(character)
    bach(character)
    much(character)
    noreplace_write(text, character.room['setting'])

def cheat_ending1(character):
    end1_command(character)
    character.status = 'end1'
    
def cheat_ending2(character):
    character.loc = [3.5,3]
    chooseroom(character)
    bach(character)
    much(character)
    write(text, character.room['setting'])
    character.status = 'end2'
    
def end2_enter(character):
    write(text, 'Congratulations! You successfully escaped the deserted island in ' + str(character.token + 1) + '''
turns!
Nice job on finding the secret ending! But perhaps you haven't had
the chance to complete the regular ending... (although, considering
your newfound powers, ought to be all to easy.(if you can figure out
how you should use them!))
Do you want to continue playing? (yes/no)''')

def credits_command():
    write(text, '''
Despite the game being a group effort, we all had things that we
especially worked on. These can be seen below.
Ella Huang: Main Writer
Jennifer Du: Main Artist
Laura Wrigley-Carr: Tech Support
Also, many thanks to Gavin Carr, for being the Tech Support for when
the Tech Support failed.
''')

def swim_command(character):
    if character.room == beach1:
        write(text, '''You swim for about 100m before it occurs to you that this is a very 
bad idea.''')
    elif character.room == waterfall1:
        write(text, '''You jump in the pool of water and splash around for a while. Your
morale increased, but not sure how this is supposed to help you get off the island...?''')
    else:
        write(text, 'You writhe around on the ground, but nothing happens. Odd...')

def jump_command(character):
    if character.room == cliff1:
        write(text, '''...Ok then? You jump off the cliff to your death. Such a sorrowful
waste of life...
Why do you suddenly think of tacos? One of life's many mysteries...''')
        death(character)
    else:
        write(text, '''You search for something to jump off of, but sadly there are no cliffs
around here.
But then, You reflect, life is such a precious thing...''')

def health_check(turn_no, character):
    #This is turn-based health deductor
    if turn_no < 5:
        turn_no = turn_no + 1
    else:
        character.health = character.health - 1
        turn_no = 0

def health_warning(character):
    #Low health warning
    if character.health <= 5 and character.health >= 1:
        noreplace_write(text, 'Caution! Your health is ' + str(character.health) + '''/20! if you do not
regain health soon, you will DIE!!!''')
    else:
        noreplace_write(text, '''
You have ''' + str(character.health) + '''/20 HP.''')

def starvation_check(character):
    #Death by starvation
    if character.health <= 0:
        write(text, '''You stumble a few paces. You slowly sway, and then fall into the dirt,
utterly exhausted. You do not move again...''')
        death(character)
