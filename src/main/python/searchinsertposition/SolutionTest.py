import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(6, sol.searchInsert([1,3,4,6,7,10], 11))
        self.assertEqual(0, sol.searchInsert([1], 1))
        self.assertEqual(0, sol.searchInsert([1], 0))
        self.assertEqual(0, sol.searchInsert([1, 3, 5, 6], 0))

        ans3 = "a"


if __name__ == '__main__':
    unittest.main()
