from rooms import *
import items
import gfunctions
from classes import Output
import initalisation
import tkintermaker
from gfunctions import chooseroom, get, invcheck

write = Output.write
noreplace_write = Output.noreplace_write
#Pass in character in the brackets!!!!!


def help_command():
    write(tkintermaker.text, """You hear a mysterious voice coming from the nearest place of
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
examine/ex - In some settings, there are mini-locations that you can
             enter - as indicated by the description
enter/exit - can be used to enter or exit a mini-location inside a
room, as indicated by description
rest - used to restore 10 HP - can only be done inside safe location

If you need help on a specific topic, type 'topics' in the help 
prompt, and I will list the topics I can assist you on. If you wish
to leave the MHS, type 'leave' to exit the help station.

Please note, some commands are secret, and must be discovered for 
yourself.
Good luck, Traveller....
(The voice fades away)""")
    
    while True:
        helpcommand = input('help> ')
        helpcmd = parsecommand(helpcommand)

        if helpcmd.verb == 'leave':
            break
        
        elif helpcmd.verb in ['topics']:
            write(tkintermaker.text, '''Topics I can tell you about are:
                          - game
                          - food
                          - crafting
                          - HP
                          - 
                    ''')
        elif helpcmd.verb == 'game':
            write(tkintermaker.text, '''The desert island game is a game where you are trapped on a deserted
island. The aim of the game is to survive, and eventually make your
escape.''')
        elif helpcmd.verb == 'food':
            write(tkintermaker.text, '''Food can be used in the game to restore HP. It can be stored in the
inventory until time of consumption, at which point it will be 
removed from the inventory.''')
        elif helpcmd.verb == 'crafting':
            write(tkintermaker.text, '''Crafting is where you combine multiple different items together into
a new item. This can be done using the 'make' command, written as 
'make [item]', and if you have all the neccasary items for the item,
it will be created and put into your inventory. The items used to 
make it will then be erased.''')
        elif helpcmd.verb in ['HP', 'hp', 'health']:
            write(tkintermaker.text, '''Health points, or HP, is a way of measuring a characters health. If
your HP reaches 0, you will DIE!!!! In order to regain HP, you can
eat food or rest in a safe place. You will lose HP through moving
from place to place and gradual starvation(1 HP every 5 turns)''')


def look_command(character):
    write(tkintermaker.text, character.room['setting'])
    
def items_command(character):
    name_list = [i['name'] for i in character.room['items']]
    write(tkintermaker.text, ', '.join(name_list))



def get_command(cmd, character, item):
    if cmd.item == 'trout' and character.room == rocks:
        write(tkintermaker.text, '''You try to grab the trout.... But it eludes you, staring back in 
disdain.''')
        write(tkintermaker.text, 'If only you had something to catch it in...')
        #continue
    if cmd.item == 'seagull' and character.room == beach:
        write(tkintermaker.text, 'You try to grab the seagull... but it poops on your head.')
        #continue
    if item in character.room['items'] and item['getable']and len(character.inventory) < 10:
        write(tkintermaker.text, 'You picked up the ' + cmd.item)
        character.room['items'].remove(item)
        get(item, character)
    elif len(character.inventory) == 10:
        write(tkintermaker.text, 'Sorry, your inventory is full. You cannot carry more than 10 items.')
    elif item not in character.room['items']:
        write(tkintermaker.text, 'get... what? That ain\'t even in this place!')
    elif not item['getable']:
        write(tkintermaker.text, 'You can\'t pick that up!')


def use_command(character):
    if item in toolslist and character.inventory:
        if item in character.room['tools']:
            get(item['getitem'])
            write(tkintermaker.text, item['string'])
    elif item in toolslist:
        write(tkintermaker.text, 'You don\'t have one of those!')
    elif item in character.inventory:
        write(tkintermaker.text, 'You can\'t use that!')
    else:
        write(tkintermaker.text, 'What??? You can\'t use something you don\'t have which is not a tool!!')
            
def inventory_command(character):
    if len(character.inventory) > 0:
        inventory_list = [i['name'] + '(' + str(i['inv']) + ')' for i in character.inventory]
        write(tkintermaker.text, ', '.join(inventory_list))
    else:
        write(tkintermaker.text, "You have nothing in your inventory... so sad.")

def eat_command(cmd, character, item):
    if item == 'null':
        write(tkintermaker.text, 'What do you want to eat?')
    if item and item['edible'] and item in character.inventory:
        if character.health < 20:
            write(tkintermaker.text, 'You eat the ' + cmd.item)
            if item == items.berry:
                if random.randint(1,2) == 1:
                    berry['health'] = 10
                else:
                    write(tkintermaker.text, 'It seems the berry was poisoned! You lost 10 health points!')
                    berry['health'] = -10
            item['inv'] = item['inv'] - 1
            invcheck(character)
            character.health = character.health + item['health']
            if character.health > 20:
                character.health = 20
            write(tkintermaker.text, 'Your health level is now ' + str(character.health) + '/20')
        else:
            write(tkintermaker.text, 'You aren\'t in need of energy just now')
            #continue
    elif item not in character.inventory:
        write(tkintermaker.text, 'You don\'t even have that, silly!')
    elif not item['edible']:
        write(tkintermaker.text, 'You want to eat that? No. Just... no.')

def health_command(character):
    write(tkintermaker.text, 'You have ' + str(character.health) + '/20 HP.')
    #continue

def west_command(character):
    if character.room in [waterfall, jungle, beach]:
        write(tkintermaker.text, 'You walk to the west.')
        character.loc[1] = character.loc[1] - 1
        chooseroom(character)
        noreplace_write(tkintermaker.text, 'You are now at the ' + character.room['locname'])
        noreplace_write(tkintermaker.text, character.room['setting'])
        character.health = character.health - 2
    else:
        write(tkintermaker.text, 'You can\'t go that way!')
    
def east_command(character):
    if character.room in [mountains, village, rocks]:
        write(tkintermaker.text, 'You walk to the east.')
        character.loc[1] = character.loc[1] + 1
        chooseroom(character)
        noreplace_write(tkintermaker.text, 'You are now at the ' + character.room['locname'])
        noreplace_write(tkintermaker.text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(tkintermaker.text, 'You can\'t go that way!')
          
def north_command(character):
    if character.room in [beach, jungle, hill, cliff]:
        write(tkintermaker.text, 'You walk to the north.')
        character.loc[0] = character.loc[0] + 1
        chooseroom(character)
        noreplace_write(tkintermaker.text, 'You are now at the ' + character.room['locname'])
        noreplace_write(tkintermaker.text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(tkintermaker.text, 'You can\'t go that way!')
          
def south_command(character):
    if character.room in [mountains, waterfall, jungle, hill]:
        write(tkintermaker.text, 'You walk to the south.')
        character.loc[0] = character.loc[0] - 1
        chooseroom(character)
        noreplace_write(tkintermaker.text, 'You are now at the ' + character.room['locname'])
        noreplace_write(tkintermaker.text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(tkintermaker.text, 'You can\'t go that way!')    


def examine_command(item):
    write(tkintermaker.text, 'This is the info on the ' + item['name'])
    noreplace_write(tkintermaker.text, 'Name: ' + item['name'])
    noreplace_write(tkintermaker.text, 'Description: ' + item['desc'])
    noreplace_write(tkintermaker.text, 'Getable: ' + str(item['getable']))
    noreplace_write(tkintermaker.text, 'Edible: ' + str(item['edible']))
    noreplace_write(tkintermaker.text, 'Usable: ' + str(item['usable']))
    noreplace_write(tkintermaker.text, 'HP avaliable: ' + str(item['health']))


def enter_command(character):
    if character.room in [jungle, village]:
        character.loc[0] = character.loc[0] + 0.5
        chooseroom(character)
        write(tkintermaker.text, 'You enter the ' + character.room['locname'])

def exit_command(character):
    if character.room in [clearing]:
        write(tkintermaker.text, 'You exit the ' + character.room['locname'])
        character.loc[0] = character.loc[0] - 0.5
        chooseroom(character)

def rest_command(character):
    if character.room in [clearing, house]:
        write(tkintermaker.text, 'You lie down on the soft ground. You slowly drift into sleep...')
        noreplace_write(tkintermaker.text, 'Your HP increased by 10.')
        character.health = character.health + 10
        if character.health > 20:
            character.health = 20
    else:
        write(tkintermaker.text, '''Dude, what kind of survivalist sleeps in a potentially hostile 
location???''')

def teleport_command(character):
    for i in roomslist:
        if i['locname'] == cmd.item:
            write(tkintermaker.text, 'Success! You have teleported to the ' + i['locname'])
            character.loc = i['location']
            chooseroom(character)

    
    
def _get_command(character, item):
    if item in itemslist:
        if len(character.inventory) > 10:
            write(tkintermaker.text, '''Caution! Your inventory is less than 10! In order to \'get\' things,
you will need to keep your items under 10!''')
        get(item, character)
    else:
        write(tkintermaker.text, 'not real, dude.')
        #continue


def _die_command():
    death()

def _five_command(character):
    character.health = character.health - 5



def error_command():
    write(tkintermaker.text, '''I\'m sorry, but that is not a valid command. If you require assistance,
please consult the MHS by typing help''')
    #continue



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
        write(tkintermaker.text, 'Caution! Your health is ' + str(character.health) + '''/20! if you do not
regain health soon, you will DIE!!!''')
    else:
        noreplace_write(tkintermaker.text, '''
You have ''' + str(character.health) + '''/20 HP.''')

def starvation_check(character):
    #Death by starvation
    if character.health <= 0:
        write(tkintermaker.text, '''You stumble a few paces. You slowly sway, and then fall into the dirt,
utterly exhausted. You do not move again...''')
        death()