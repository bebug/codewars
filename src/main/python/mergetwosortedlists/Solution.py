import unittest
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

class Solution:

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = None
        current: ListNode = None
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val <= l2.val:
                    result, current = self.addToListNode(result, current, l1.val)
                    l1 = l1.next
                else:
                    result, current = self.addToListNode(result, current, l2.val)
                    l2 = l2.next

            elif l1 is not None:
                result, current = self.addToListNode(result, current, l1.val)
                l1 = l1.next
            else:
                result, current = self.addToListNode(result, current, l2.val)
                l2 = l2.next
        return result

    def addToListNode(self, result: Optional[ListNode], current: Optional[ListNode], val) -> (ListNode, ListNode):
        if result is None:
            result = ListNode(val)
            current = result
            return result, current
        else:
            ln = ListNode(val)
            current.next = ln
            current = ln
        return result, current
