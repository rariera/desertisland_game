import gfunctions

def health_check():
    #This is turn-based health deductor
    if it.turn_no < 5:
        turn_no = it.turn_no + 1
    else:
        character.health = character.health - 1
        turn_no = 0

def health_warning():
    #Low health warning
    if character.health <= 5 and character.health >= 1:
        write(text, 'Caution! Your health is ' + str(character.health) + '''/20! if you do not
regain health soon, you will DIE!!!''')
    else:
        write(text, 'You have ' + str(character.health) + '/20 HP.')

def starvation_check():
    #Death by starvation
    if character.health <= 0:
        write(text, '''You stumble a few paces. You slowly sway, and then fall into the dirt,
utterly exhausted. You do not move again...''')
        death()
