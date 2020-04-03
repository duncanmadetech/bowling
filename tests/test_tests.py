import unittest
from bowling.bowl import Bowl
import random

# Each two attempt is called a go
# There are ten goes in a frame

class TestTests(unittest.TestCase):

    def test_can_score(self):
        score = random.randint(1, 9)
        game = Bowl()
        game.score(score)
        self.assertEqual(score, game.get_score())

    def test_can_score_from_two_goes(self):
        game = Bowl()
        game.score(5)
        game.score(7)
        self.assertEqual(12, game.get_score())

    def test_initial_score_is_zero(self):
        self.assertEqual(0, Bowl().get_score())
