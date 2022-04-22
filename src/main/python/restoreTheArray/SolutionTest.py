import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(411743991, sol.numberOfArrays("600342244431311113256628376226052681059918526204", 703))
        self.assertEqual(8, sol.numberOfArrays("1317", 2000))
        self.assertEqual(0, sol.numberOfArrays("1000", 10))
        self.assertEqual(1, sol.numberOfArrays("1000", 10000))


if __name__ == '__main__':
    unittest.main()
