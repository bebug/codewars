import unittest
import sys
import os

path = os.path.abspath(__file__)
sys.path.insert(0, os.path.abspath("./../../../main/python/reversedarrayofdigits"))
import reversedArrayOfDigits as rad


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([0,2,9,3,9,8,2,6,7,5,4], rad.digitize(45762893920))


if __name__ == '__main__':
    unittest.main()
