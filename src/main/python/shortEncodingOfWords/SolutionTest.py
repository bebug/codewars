import unittest
from Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(10, sol.minimumLengthEncoding(["time", "me", "bell"]))


if __name__ == '__main__':
    unittest.main()
