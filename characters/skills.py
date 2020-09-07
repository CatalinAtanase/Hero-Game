from .skills_actions import rapid_strike_action, magic_shield_action

'''
return a dictionary that can be appended 
to the player skills 
'''
def rapid_strike(name):
    return {
        'name': 'Rapid strike',
        'action': rapid_strike_action,
        'chance': 10,
        'description': f'{name} attacks twice this turn.'
    }

def magic_shield(name):
    return {
        'name': 'Magic shield',
        'action': magic_shield_action,
        'chance': 20,
        'description': f'{name} takes only half of the usual damage.'
    }