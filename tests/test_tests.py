import unittest
from bowling.bowl import Bowl
import random

# https://learn.madetech.com/katas/bowling/
# Each bowl is called a throw
# Each two attempt is called a frame
# There are ten frames in a line

class TestTests(unittest.TestCase):

    def test_can_score_a_frame(self):
        game = Bowl()
        game.score(5, 3)
        self.assertEqual(8, game.get_score())

    def test_scoring_a_spare_will_add_on_the_next_bowl_to_the_previous_score(self):
        game = Bowl()
        game.score(4, 6)
        game.score(6, 2)
        self.assertEqual(24, game.get_score())

    def test_you_can_score_a_strike(self):
        game = Bowl()
        game.strike()
        self.assertEqual(10, game.get_score())

    def test_initial_score_is_zero(self):
        self.assertEqual(0, Bowl().get_score())
