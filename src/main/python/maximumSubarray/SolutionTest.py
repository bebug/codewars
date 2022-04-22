import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(-1, sol.maxSubArray(list([-1])))
        self.assertEqual(6, sol.maxSubArray(list([1, 2, 3])))
        self.assertEqual(1, sol.maxSubArray(list([1])))
        self.assertEqual(23, sol.maxSubArray(list([5,4,-1,7,8])))

if __name__ == '__main__':
    unittest.main()
