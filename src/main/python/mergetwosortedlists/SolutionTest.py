import unittest
from Solution import Solution
from Solution import ListNode

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(val=arr[0], next=list_to_LL(arr[1:]))

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sol = Solution()

        self.assertEqual(str(list_to_LL([1, 2, 2, 3, 3, 4])), str(sol.mergeTwoLists(list_to_LL([1, 2, 3]), list_to_LL([2, 3, 4]))))


if __name__ == '__main__':
    unittest.main()
