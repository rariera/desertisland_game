from cfunctions import *
from classes import *
import tkintermaker


global character
character = Character(loc = [1,2], health = 20, inventory = [])



def check_command(cmd, item, collection, toolslist, makelist):
    verbiage = False
    if cmd.verb in ['help', 'h']:
        help_command()
    elif cmd.verb in ['look', 'l']:
        verbiage = look_command(character)
    elif cmd.verb == '_items':
        verbiage = items_command(character.room)
    elif cmd.verb in ['get']:
        get_command(cmd, character, item)
    elif cmd.verb in ['use', 'u']:
        use_command(character, item, toolslist)
    elif cmd.verb in ['inventory', 'i']:
        inventory_command(character)
    elif cmd.verb in ['eat']:
        eat_command(cmd, character, item)
    elif cmd.verb == 'health':
        health_command(character)
    elif cmd.verb in ['west','w']:
        west_command(character)
    elif cmd.verb in ['east','e']:
        east_command(character)
    elif cmd.verb in ['north','n']:
        north_command(character)
    elif cmd.verb in ['south','s']:
        south_command(character)
    elif cmd.verb in ['examine', 'ex']:
        examine_command(item)
    elif cmd.verb in ['enter']:
        enter_command(character)
    elif cmd.verb in ['exit']:
        exit_command(character)
    elif cmd.verb in ['rest', 'r']:
        rest_command(character)
    elif cmd.verb == '_teleport':
        teleport_command(character, cmd)
    elif cmd.verb == 'make':
        make_command(item, character, makelist)
    elif cmd.verb == '_get':
        cget_command(character, item, collection)
    elif cmd.verb == '_die':
        _die_command()
    elif cmd.verb == '_five':
        _five_command(character)
    else:
        error_command()

    if verbiage:
        write(tkintermaker.text, verbiage)

def chealth_check(turn_no):
    health_check(turn_no, character)
def chealth_warning():
    health_warning(character)
def cstarvation_check():
    starvation_check(character)
