from gameplay.actions import play_game
from characters.hero import Hero
from characters.beast import Beast
from gameplay.utils import declare_winner, game_intro

if __name__ == "__main__":
    '''
    create both the hero and the beast
    '''
    hero = Hero()
    beast = Beast()
    turn_number = 1

    # Just printing the introduction
    game_intro()

    print(hero)
    print(beast)

    # Check for the better speed or luck, if equal the hero will start
    if hero.speed > beast.speed:
        play_game(hero, beast, turn_number)
    elif beast.speed > hero.speed:
        play_game(beast, hero, turn_number)
    elif hero.luck >= beast.luck:
        play_game(hero, beast, turn_number)
    else:
        play_game(beast, hero, turn_number)

    declare_winner(hero, beast)
