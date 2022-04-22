import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual('eetr', sol.frequencySort('tree'))
        self.assertEqual('aaaccc', sol.frequencySort('cccaaa'))
        self.assertEqual('bbAa', sol.frequencySort('Aabb'))

if __name__ == '__main__':
    unittest.main()
