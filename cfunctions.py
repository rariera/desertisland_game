import rooms
import items
import tools
import gfunctions
from tkintermaker import Output
import initalisation


def help_command():
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

                  
def look_command():
    write(text, character.room['setting'])
    
def items_command():
    name_list = [i['name'] for i in character.room['items']]
    write(text, ', '.join(name_list))



def get_command():
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


def use_command():
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
            
def inventory_command():
    if len(character.inventory) > 0:
        inventory_list = [i['name'] + '(' + str(i['inv']) + ')' for i in character.inventory]
        write(text, ', '.join(inventory_list))
    else:
        write(text, "You have nothing in your inventory... so sad.")
    #continue

def eat_command():
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

def health_command():
    write(text, 'You have ' + str(character.health) + '/20 HP.')
    #continue

def west_command():
    if character.loc[1] in [2]:
        write(text, 'You walk to the west.')
        character.loc[1] = character.loc[1] - 1
        chooseroom(character)
        write(text, 'You are now at the ' + character.room['locname'])
        write(text, character.room['setting'])
        character.health = character.health - 2
    else:
        write(text, 'You can\'t go that way!')
    
def east_command():
    if character.loc[0] in [1] and character.loc[1] in [1]:
        write(text, 'You walk to the east.')
        character.loc[1] = character.loc[1] + 1
        chooseroom(character)
        write(text, 'You are now at the ' + character.room['locname'])
        write(text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(text, 'You can\'t go that way!')
          
def north_command():
    if character.loc[0] in [1,2] and character.loc[1] in [2,3]:
        write(text, 'You walk to the north.')
        character.loc[0] = character.loc[0] + 1
        chooseroom(character)
        write(text, 'You are now at the ' + character.room['locname'])
        write(text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(text, 'You can\'t go that way!')
          
def south_command():
    if character.loc[0] in [3,2] and character.loc[1] in [2,3]:
        write(text, 'You walk to the south.')
        character.loc[0] = character.loc[0] - 1
        chooseroom(character)
        write(text, 'You are now at the ' + character.room['locname'])
        write(text, character.room['setting'])
        character.health = character.health - 2
    else:
          write(text, 'You can\'t go that way!')    


def examine_command():
    write(text, 'This is the info on the ' + item['name'])
    write(text, 'Name: ' + item['name'])
    write(text, 'Description: ' + item['desc'])
    write(text, 'Getable: ' + str(item['getable']))
    write(text, 'Edible: ' + str(item['edible']))
    write(text, 'Usable: ' + str(item['usable']))
    write(text, 'HP avaliable: ' + str(item['health']))


def enter_command():
    if character.room in [jungle]:
        character.loc[0] = character.loc[0] + 0.5
        chooseroom(character)
        write(text, 'You enter the ' + character.room['locname'])

def exit_command():
    if character.room in [clearing]:
        write(text, 'You exit the ' + character.room['locname'])
        character.loc[0] = character.loc[0] - 0.5
        chooseroom(character)

def rest_command():
    if character.room in [clearing]:
        write(text, 'You lie down on the soft ground. You slowly drift into sleep...')
        write(text, 'Your HP increased by 10.')
        character.health = character.health + 10
        if character.health > 20:
            character.health = 20
    else:
        write(text, 'Dude, what kind of survivalist sleeps in a potentially hostile location???')

def teleport_command():
    for i in roomslist:
        if i['locname'] == cmd.item:
            write(text, 'Success! You have teleported to the ' + i['locname'])
            character.loc = i['location']
            chooseroom(character)

    
    
def _get_command():
    if item in itemslist:
        if len(character.inventory) > 10:
            write(text, '''Caution! Your inventory is less than 10! In order to \'get\' things, you will need to
                  keep your items under 10!''')
        get(item)
    else:
        write(text, 'not real, dude.')
        #continue


def _die_command():
    death()

def _five_command():
    character.health = character.health - 5



def error_command():
    write(text, '''I\'m sorry, but that is not a valid command. If you require assistance,
please consult the MHS by typing help''')
    #continue

