from gameplay.utils import is_done, print_turn_number, load_round
from .result import result
import random

'''
Check if the defender is lucky,
if lucky just go ahead and print the result else
calculate the damage to be done and then
let the defender do his defensive skills

If damage_to_be_done > 0 go ahead and substract that
from the defender health
'''
def attack(attacker, defender):
    lucky = False

    if is_lucky(defender):
        lucky = True
    else:
        attacker.damage_to_be_done = attacker.strength - defender.defence
        defender.do_skills(attacker, defender, defender.defensive_skills, False)
        if attacker.damage_to_be_done > 0:
            defender.health -= attacker.damage_to_be_done
    
    result(attacker, defender, lucky, attacker.damage_to_be_done)

# Check if the character is lucky
def is_lucky(character):
    return True if character.luck >= random.randint(0, 100) else False


def play_game(player1, player2, turn_number):
    '''
    As long as the players have positive hp
    and the turn_number is less than 20 keep going
    '''
    while not is_done(player1, player2, turn_number):
        load_round()
        print_turn_number(turn_number)

        '''
        Cast all the offensive skills before the attack
        '''
        player1.do_skills(player1, player2, player1.offensive_skills, True)
        attack(player1, player2)

        '''
        If the second player still has positive hp,
        he can procede with his attack
        '''
        if player2.health > 0:
            player2.do_skills(player2, player1, player2.offensive_skills, True)
            attack(player2, player1)
        
        turn_number += 1