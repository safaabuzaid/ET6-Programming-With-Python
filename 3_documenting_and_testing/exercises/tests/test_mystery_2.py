import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ """

    def test_minimal_list_input(self):
        """"""
        self.assertEqual(mystery_2([]), None)

    def test_minimal_string_input(self):
        """"""
        self.assertEqual(mystery_2(''), None)

    def test_numbers(self):
        self.assertEqual(mystery_2([5,4,3]),3)

    def test_negatives(self):
        self.assertEqual(mystery_2([-4,-3,-7]),3)

    def test_characters(self):
        self.assertEqual(mystery_2('Safaa'),5)
