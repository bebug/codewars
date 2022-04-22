from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(neededTime) == 0:
            return 0
        poptime = 0
        lastColor = colors[0]
        lastPosition = 0
        for i in range(1, len(colors)):
            color = colors[i]
            if color == lastColor:
                if neededTime[lastPosition] < neededTime[i]:
                    poptime = poptime + neededTime[lastPosition]
                    lastColor = colors[i]
                    lastPosition = i
                else:
                    poptime = poptime + neededTime[i]
            else:
                lastColor = colors[i]
                lastPosition = i

        return poptime