import os
import unittest

import sys

path = os.path.abspath(__file__)
sys.path.insert(0, os.path.abspath("./../../../main/python/leapyears"))
import leapYears as ly


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(ly.isLeapYear(1984), True)
        self.assertEqual(ly.isLeapYear(2000), True)
        self.assertEqual(ly.isLeapYear(1234), False)
        self.assertEqual(ly.isLeapYear(1234), False)
if __name__ == '__main__':
    unittest.main()
