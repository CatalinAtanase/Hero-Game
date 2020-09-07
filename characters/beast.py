from .character import Character

class Beast(Character):
    name = 'Wild Beast'
    
    # Minimum values for attributes
    min_health = 60
    min_strength = 60
    min_defence = 40
    min_speed = 40
    min_luck = 25
    
    # Maximum values for attributes
    max_health = 90
    max_strength = 90
    max_defence = 60
    max_speed = 60
    max_luck = 40

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)