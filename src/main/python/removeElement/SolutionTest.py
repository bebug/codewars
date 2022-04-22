import unittest
from Solution import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertList(list([3,2,2,3]), list([2,2]), 3)

    def assertList(self, inputList:list, answerList:list, val: int):
        sol = Solution()
        self.assertEqual(len(answerList), sol.removeElement(inputList, val))
        for i in range(len(answerList)):
            self.assertEqual(answerList[i], inputList[i])

if __name__ == '__main__':
    unittest.main()
