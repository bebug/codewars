from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        stepsize = len(nums) - 1
        result = 0

        while not(result <= 0 and nums[0] >= target) and not(result >= len(nums)) and not(nums[result - 1] < target and target <= nums[result]):
            if nums[result] < target:
                stepsize = max(1, abs(stepsize))
            else:
                stepsize = -max(1, abs(stepsize))
            result += stepsize
            stepsize = stepsize // 2

        return min(result, len(nums))