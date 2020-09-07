from unittest.mock import Mock
from gameplay.utils import game_intro, is_done, load_round, print_turn_number
from gameplay.actions import attack, play_game
from characters.beast import Beast
from characters.hero import Hero
import unittest


class ActionTest(unittest.TestCase):
    hero = Hero()
    beast = Beast()

    def test_lucky_dodge(self):
        hero = Hero()
        beast = Beast()
        
        initial_health = beast.health
        beast.luck = 100

        attack(hero, beast)

        self.assertEqual(initial_health, beast.health)

    def test_damage_done(self):
        hero = Hero()
        beast = Beast()

        # as much as the beast has defence
        hero.strength = 40
        initial_health = beast.health

        attack(hero, beast)

        self.assertEqual(initial_health, beast.health)

    def test_attack(self):
        hero = Hero()
        beast = Beast()

        hero.strength = 80
        beast.luck = 0
        initial_health = beast.health

        attack(hero, beast)

        self.assertNotEqual(initial_health, beast.health)

    def test_dmg_to_be_done(self):
        hero = Hero()
        beast = Beast()

        hero.strength = 80
        initial_dmg = hero.damage_to_be_done
        beast.luck = 0

        attack(hero, beast)

        self.assertNotEqual(initial_dmg, hero.damage_to_be_done)

    def test_is_done(self):
        hero = Hero()
        beast = Beast()
        self.assertTrue(is_done(hero, beast, 25))
        self.assertFalse(is_done(hero, beast, 18))
        hero.health = -1
        self.assertTrue(is_done(hero, beast, 18))
        hero.health = 1
        beast.health = -2
        self.assertTrue(is_done(hero, beast, 18))

    def test_play_game(self):
        hero = Hero()
        beast = Beast()
        turn_number = 1
        mock = Mock()
        expected = [is_done(hero, beast, turn_number), load_round(), print_turn_number(turn_number), hero.do_skills(hero, beast, hero.offensive_skills, True), attack(hero, beast), beast.do_skills(beast, hero, beast.offensive_skills, True), attack(beast, hero)]
        mock.play_game(hero, beast, turn_number)
        mock.mock_calls == expected


                     
      
