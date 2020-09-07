from unittest.mock import MagicMock, patch
from gameplay.actions import attack
import unittest
from unittest.mock import Mock
from characters.skills_actions import magic_shield_action, rapid_strike_action
from characters.skills import magic_shield, rapid_strike
from characters.hero import Hero
from characters.beast import Beast


class TestHero(unittest.TestCase):
    hero = Hero()
  
    def test_name(self):
        self.assertEqual(self.hero.name, 'Orderus')

    def test_attribute_health(self):
        self.assertTrue(self.hero.health >= 70 and self.hero.health <= 100)

    def test_attribute_strength(self):
        self.assertTrue(self.hero.strength >= 70 and self.hero.strength <= 80)

    def test_attribute_defence(self):
        self.assertTrue(self.hero.defence >= 45 and self.hero.defence <= 55)

    def test_attribute_speed(self):
        self.assertTrue(self.hero.speed >= 40 and self.hero.speed <= 50)

    def test_attribute_luck(self):
        self.assertTrue(self.hero.luck >= 10 and self.hero.luck <= 30)

    def test_offensive_skills(self):
        self.assertTrue(self.hero.offensive_skills)

    def test_defensive_skills(self):
        self.assertTrue(self.hero.defensive_skills)


class TestBeast(unittest.TestCase):
    beast = Beast()

    def test_name(self):
        self.assertEqual(self.beast.name, 'Wild Beast')

    def test_attribute_health(self):
        self.assertTrue(self.beast.health >= 60 and self.beast.health <= 90)

    def test_attribute_strength(self):
        self.assertTrue(self.beast.strength >= 60 and self.beast.strength <= 90)

    def test_attribute_defence(self):
        self.assertTrue(self.beast.defence >= 40 and self.beast.defence <= 60)

    def test_attribute_speed(self):
        self.assertTrue(self.beast.speed >= 40 and self.beast.speed <= 60)

    def test_attribute_luck(self):
        self.assertTrue(self.beast.luck >= 25 and self.beast.luck <= 40)
    
    def test_offensive_skills(self):
        self.assertFalse(self.beast.offensive_skills)

    def test_defensive_skills(self):
        self.assertFalse(self.beast.defensive_skills)


class SkillsTest(unittest.TestCase):

    def test_rapid_strike(self):
        self.assertEqual(rapid_strike('Player')['action'], rapid_strike_action)

    def test_magic_shield(self):
        self.assertEqual(magic_shield('Player')['action'], magic_shield_action)


class SkillsActionsTest(unittest.TestCase):
    mock = Mock()
    hero = Hero()
    beast = Beast()

    def test_magic_shield_action(self):
        hero = Hero()
        beast = Beast()

        beast.luck = 0
        attack(hero, beast)
        initial_dmg_to_be_done = hero.damage_to_be_done
        self.assertTrue(initial_dmg_to_be_done > 0)

        magic_shield_action(hero, beast)

        self.assertTrue(hero.damage_to_be_done == initial_dmg_to_be_done // 2)

    def test_rapid_strike_action(self):
        hero = Hero()
        beast = Beast()
        mock = Mock()
        expected = [attack(hero, beast)]
        mock.rapid_strike_action(hero, beast)
        mock.mock_calls == expected




        