import unittest
from bowling.bowl import Bowl
import random

# https://learn.madetech.com/katas/bowling/
# Each bowl is called a throw
# Each two attempt is called a frame
# There are ten frames in a line

class TestTests(unittest.TestCase):

    def test_can_score_a_throw(self):
        score = random.randint(1, 9)
        game = Bowl()
        game.score(score)
        self.assertEqual(score, game.get_score())

    def test_can_score_a_frame(self):
        game = Bowl()
        game.score(5)
        game.score(3)
        self.assertEqual(8, game.get_score())

    def test_initial_score_is_zero(self):
        self.assertEqual(0, Bowl().get_score())
