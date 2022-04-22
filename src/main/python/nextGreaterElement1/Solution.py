from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        positionDict = {}
        for num in reversed(nums2):
            while len(stack) > 0:
                nextGreater = stack[len(stack) -1]
                if (nextGreater > num):
                    positionDict[num] = nextGreater
                    break
                else:
                    stack.pop()

            if len(stack) == 0:
                positionDict[num] = -1
            stack.append(num)

        return [positionDict[x] for x in nums1]
