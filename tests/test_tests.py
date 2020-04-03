import unittest
from bowling.bowl import Bowl

# Each pair throws is called a game
# There are ten games in a frame

class TestTests(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(True)

    def test_can_score(self):
        game = Bowl()
        game.score(5)
        self.assertEqual(5, game.get_score())
