import random

class Character:
    name = None
    damage_to_be_done = None

    # Minimum values for attributes
    min_health = None
    min_strength = None
    min_defence = None
    min_speed = None
    min_luck = None
    
    # Maximum values for attributes
    max_health = None
    max_strength = None
    max_defence = None
    max_speed = None
    max_luck = None

    offensive_skills = None
    defensive_skills = None
    
    # Set attributes to random values
    def __init__(self):
        self.health = self.set_property(self.min_health, self.max_health)
        self.strength = self.set_property(self.min_strength, self.max_strength)
        self.defence = self.set_property(self.min_defence, self.max_defence)
        self.speed = self.set_property(self.min_speed, self.max_speed)
        self.luck = self.set_property(self.min_luck, self.max_luck)
        self.set_skills()

    # return a random value 
    def set_property(self, min_value, max_value):
        return random.randint(min_value, max_value)

    # Set skills at the beggining for both the hero and the beast
    def set_skills(self):
        self.offensive_skills = []
        self.defensive_skills = []
        

    def __str__(self):
        return f'''
        {self.name} has: 
            {self.health} health
            {self.strength} strength
            {self.defence} defence
            {self.speed} speed
            {self.luck} luck '''

    # Cast all the available skills
    def do_skills(self, attacker, defender, type_of_skills, state):
        number_of_skills_done = 0
        for skill in type_of_skills:
            if skill['chance'] >= random.randint(0, 100):
                number_of_skills_done += 1
                self.print_skill(skill)
                skill['action'](attacker, defender)

        if number_of_skills_done == 0:
            if state:
                self.print_no_skills_done('attacking')
            else:
                self.print_no_skills_done('defending')

    def print_skill(self, skill):
        print(f''' 
            {skill['name']} has been used.
            {skill['description']}'''
        )

    def print_no_skills_done(self, state):
        print(f''' 
            No skills done by {self.name} while {state}.'''
        )