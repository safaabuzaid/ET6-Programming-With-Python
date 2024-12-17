import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_3(0, 0), 0)
    
    def test_1(self):
        self.assertEqual(mystery_3(3,6),3)

    def test_2(self):
        self.assertEqual(mystery_3(6,7),6)

    def test_3(self):
        self.assertEqual(mystery_3(3,3),6)
    
    def test_4(self):
        self.assertEqual(mystery_3(7,6),6)
