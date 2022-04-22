from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summary: int = 0
        result: int = -sys.maxsize-1
        for i in nums:
            if summary < 0:
                summary = i
            else:
                summary = summary+i

            result = max(result, summary)

        return result