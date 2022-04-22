import unittest
import duplicateCount as cnt

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(cnt.duplicate_count(""), 0)
        self.assertEqual(cnt.duplicate_count("abcde"), 0)
        self.assertEqual(cnt.duplicate_count("abcdeaa"), 1)
        self.assertEqual(cnt.duplicate_count("abcdeaB"), 2)
        self.assertEqual(cnt.duplicate_count("Indivisibilities"), 2)


if __name__ == '__main__':
    unittest.main()
