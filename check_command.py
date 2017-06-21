def check_command():
    if cmd.verb in ['help', 'h']:
        help_command()
    elif cmd.verb in ['look', 'l']:
        look_command()
    elif cmd.verb == '_items':
        items_command()
    elif cmd.verb in ['get']:
        get_command()
    elif cmd.verb in ['use', 'u']:
        use_command()
    elif cmd.verb in ['inventory', 'i']:
        inventory_command()
    elif cmd.verb in ['eat']:
        eat_command()
    elif cmd.verb == 'health':
        health_command()
    elif cmd.verb in ['west','w']:
        west_command()
    elif cmd.verb in ['east','e']:
        east_command()
    elif cmd.verb in ['north','n']:
        north_command()
    elif cmd.verb in ['south','s']:
        south_command()
    elif cmd.verb in ['examine', 'ex']:
        examine_command()
    elif cmd.verb in ['enter']:
        enter_command()
    elif cmd.verb in ['exit']:
        exit_command()
    elif cmd.verb in ['rest', 'r']:
        rest_command()
    elif cmd.verb == '_teleport':
        teleport_command()
    elif cmd.verb == '_get':
        _get_command()
    elif cmd.verb == '_die':
        _die_command()
    elif cmd.verb == '_five':
        _five_command()
    else:
        error_command()
