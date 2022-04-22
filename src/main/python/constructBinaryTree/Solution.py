from typing import Optional
from typing import List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.createNode(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def createNode(self, preorder: List[int], inorder: List[int], pOStart: int, pOEnd: int, iOStart: int, iOEnd: int) -> Optional[TreeNode]:
        print("pOStart:" + str(pOStart) + " pOEnd:" + str(pOEnd) + " iOStart:" + str(iOStart) + " iOEnd:" + str(iOEnd))

        if (pOStart > pOEnd):
            return None
        value = preorder[pOStart]
        result = TreeNode(value)
        iOPosition = iOStart

        print("value:" + str(value))

        while not inorder[iOPosition] == value:
            iOPosition += 1
            print("inorder:" + str(inorder[iOPosition]) + " " + str(not inorder[iOPosition] == value))

        leftElements = iOPosition - iOStart

        result.left = self.createNode(preorder, inorder, pOStart + 1, pOStart + leftElements, iOStart, iOPosition - 1)
        result.right = self.createNode(preorder, inorder, pOStart + leftElements + 1, pOEnd, iOPosition + 1, iOEnd)


        return result