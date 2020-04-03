import unittest
from bowling.bowl import Bowl
import random

# Each pair throws is called a game
# There are ten games in a frame

class TestTests(unittest.TestCase):

    def test_can_score(self):
        score = random.randint(1, 9)
        game = Bowl()
        game.score(score)
        self.assertEqual(score, game.get_score())
