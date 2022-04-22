import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()
        self.assertEqual(3, sol.search('ababca', 'kokopkokokokopkokos'))

if __name__ == '__main__':
    unittest.main()
