import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(28, sol.uniquePaths(3, 7))

if __name__ == '__main__':
    unittest.main()
