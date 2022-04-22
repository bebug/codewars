import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(False, sol.isMatch("aa", "a"))
        self.assertEqual(True, sol.isMatch("aa", "*"))
        self.assertEqual(False, sol.isMatch("cb", "?a"))



if __name__ == '__main__':
    unittest.main()