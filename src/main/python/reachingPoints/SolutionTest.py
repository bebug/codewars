import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(False, sol.reachingPoints(2, 9, 5, 11))
        self.assertEqual(True, sol.reachingPoints(10, 5, 15, 5))
        self.assertEqual(True, sol.reachingPoints(9, 10, 9, 19))
        self.assertEqual(False, sol.reachingPoints(1, 1, 2, 2))
        self.assertEqual(False, sol.reachingPoints(35, 13, 455955547, 420098884))
        self.assertEqual(True, sol.reachingPoints(1, 1, 3, 5))
        self.assertEqual(False, sol.reachingPoints(1, 1, 2, 2))
        self.assertEqual(True, sol.reachingPoints(1, 1, 1, 1))

if __name__ == '__main__':
    unittest.main()
