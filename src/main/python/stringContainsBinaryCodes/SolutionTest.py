import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(True, sol.hasAllCodes('00110', 2))
        self.assertEqual(True, sol.hasAllCodes('00110110', 2))
        self.assertEqual(True, sol.hasAllCodes('0110', 1))
        self.assertEqual(False, sol.hasAllCodes('0110', 2))

if __name__ == '__main__':
    unittest.main()
