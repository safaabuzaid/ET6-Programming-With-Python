import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)
    
    def test_first(self):
        """"""
        self.assertEqual(mystery_1(5, 1), 6)
 
    def test_second(self):
        """"""
        self.assertEqual(mystery_1(-3,-6),-9)

    def test_type(self):
        """"""
        self.assertEqual(mystery_1(4.1,5.3),9.4)

    #def test_more(self):
    #    self. assertEqual(mystery_1(3,5,4),13)
