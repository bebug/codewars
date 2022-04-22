import math
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 > hour:
            return -1

        lower = 1
        upper = 10000000000
        if self.validate(dist, hour, lower):
            return lower
        if not self.validate(dist, hour, upper):
            return -1

        while not upper == lower:
            middle = lower + math.ceil((upper - lower) / 2)
            if middle == lower:
                middle = middle + 1
            if middle == upper:
                return upper

            if self.validate(dist, hour, middle):
                upper = middle
            else:
                lower = middle
        return upper

    def validate(self, dist: List[int], hour: float, speed: int):
        traveled = 0
        for distance in dist:
            traveled = math.ceil(traveled)
            traveled = traveled + distance/speed

        return traveled <= hour