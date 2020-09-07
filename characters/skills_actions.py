from gameplay.actions import attack

'''
Actions that will be done on call
'''
def rapid_strike_action(attacker, defender):
    attack(attacker, defender)


def magic_shield_action(attacker, defender):
    attacker.damage_to_be_done = attacker.damage_to_be_done // 2
