import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(")()())"), 4)
        self.assertEqual(sol.longestValidParentheses("))))((()(("), 2)
        self.assertEqual(sol.longestValidParentheses("(()"), 2)

        self.assertEqual(sol.longestValidParentheses("()(()"), 2)
        self.assertEqual(sol.longestValidParentheses(")))(((()()"), 4)



if __name__ == '__main__':
    unittest.main()
