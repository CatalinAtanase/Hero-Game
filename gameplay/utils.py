import time

# Check if the game is done
def is_done(hero, beast, turn_number):
    return False if hero.health > 0 and beast.health > 0 and turn_number <= 20 else True


def print_turn_number(turn_number):
    print(f'''
        ================================
        TURN #{turn_number}
        ================================'''
    )

def game_intro():
    print('''
        ================================
        WELCOME TO EMAGIA!!!
        ================================'''
    )

# Print the winner at the end of the game
def declare_winner(hero, beast):
    winner = None
    if (hero.health > beast.health) and beast.health <= 0:
        winner = hero.name
    elif (hero.health < beast.health) and hero.health <= 0:
        winner = beast.name

    if winner:
        print(f'''
        ================================
        The winner is {winner}!!!
        ================================'''
        )
    else:
        print(f'''
        ================================
        There's no winner. It's a draw.
        ================================'''
        )

def load_round():
    input("\nPress enter to continue...")