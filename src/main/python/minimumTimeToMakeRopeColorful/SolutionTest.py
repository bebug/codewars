import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(0, sol.minCost("abc", [1,2,3]))
        self.assertEqual(2, sol.minCost("aabaa", [1,2,3,4,1]))
        self.assertEqual(3, sol.minCost("abaac", [1,2,3,4,5]))


if __name__ == '__main__':
    unittest.main()
