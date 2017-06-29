from cfunctions import *
from classes import Character

global character
character = Character(loc = [1,2], health = 20, inventory = [])



def check_command(cmd, item):
	if cmd.verb in ['help', 'h']:
		help_command()
	elif cmd.verb in ['look', 'l']:
		look_command(character)
	elif cmd.verb == '_items':
		items_command(character)
	elif cmd.verb in ['get']:
		get_command(cmd, character, item)
	elif cmd.verb in ['use', 'u']:
		use_command(character)
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
		teleport_command(character)
	elif cmd.verb == '_get':
		_get_command(character, item)
	elif cmd.verb == '_die':
		_die_command()
	elif cmd.verb == '_five':
		_five_command(character)
	else:
		error_command()

print('yay!')
def chealth_check(turn_no):
	health_check(turn_no, character)
def chealth_warning():
	health_warning(character)
def cstarvation_check():
	starvation_check(character)