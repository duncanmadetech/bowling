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

    def test_you_can_score_a_strike_in_second_frame(self):
        game = Bowl()
        game.score(3, 3)
        game.strike()
        self.assertEqual(16, game.get_score())

    def test_scoring_a_strike_counts_the_next_two_bowls(self):
        game = Bowl()
        game.strike()
        game.score(3, 4)
        self.assertEqual(24, game.get_score())

    def test_scoring_two_strikes_counts_the_next_two_bowls(self):
        game = Bowl()
        game.strike() # 23
        game.strike() # 17
        game.score(3, 4) # 7
        self.assertEqual(47, game.get_score())

    def test_scoring_a_turkey(self):
        game = Bowl()
        game.strike() # 30
        game.strike() # 26
        game.strike() # 18
        game.score(6, 2) # 8
        self.assertEqual(82, game.get_score())

    def test_scoring_a_strike_normal_score_strike(self):
        game = Bowl()
        game.strike() # 18
        game.score(6, 2) # 8
        game.strike() # 17
        game.score(6, 1) # 7
        self.assertEqual(50, game.get_score())

    def test_scoring_a_strike_after_spare(self):
        game = Bowl()
        game.score(3, 7) # 20
        game.strike() # 17
        game.score(6, 1) # 7
        self.assertEqual(44, game.get_score())

    def test_scoring_a_strike_then_spare_then_mixture_are_counted_correctly(self):
        game = Bowl()
        game.strike() # 20
        game.score(3, 7) # 20
        game.strike() # 26
        game.strike() # 17
        game.score(6, 1) # 7
        self.assertEqual(90, game.get_score())

    def test_initial_score_is_zero(self):
        self.assertEqual(0, Bowl().get_score())

    def test_restricted_to_ten_frames(self):
        game = Bowl()
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertFalse(game.is_over)
        game.score(1, 1)
        self.assertTrue(game.is_over)
