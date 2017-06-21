import check_command
import rooms
import items
import tools
import gfunctions
import cfunctions
import health

def loop():
    entryget()
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

    check_command()
    health_check()
    health_warning()
    starvation_check()

    

    
    
    
    
    
    
