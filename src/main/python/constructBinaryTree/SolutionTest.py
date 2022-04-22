import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        ans2 = sol.buildTree([7,-10,-4,3,-1,2,-8,11], [-4,-10,3,-1,7,11,-8,2])
        ans = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

        ans3 = "a"


if __name__ == '__main__':
    unittest.main()
