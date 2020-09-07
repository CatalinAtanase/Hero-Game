from .character import Character
from .skills import rapid_strike, magic_shield

class Hero(Character):
    name = 'Orderus'

    # Minimum values for attributes
    min_health = 70
    min_strength = 70
    min_defence = 45
    min_speed = 40
    min_luck = 10
    
    # Maximum values for attributes
    max_health = 100
    max_strength = 80
    max_defence = 55
    max_speed = 50
    max_luck = 30

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        '''
        Add skills on the initial list
        The list is empty at the beggining,
        however there might me more skills 
        on the future
        '''
        self.offensive_skills.append(
            rapid_strike(self.name)
        )

        self.defensive_skills.append(
            magic_shield(self.name)
        )


 