import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual([-1,3,-1], sol.nextGreaterElement([4,1,2], [1,3,4,2]))
        self.assertEqual([3,-1], sol.nextGreaterElement([2,4], [1,2,3,4]))


if __name__ == '__main__':
    unittest.main()
