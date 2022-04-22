class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        start = (tx, ty)
        search = (sx, sy)

        while (search[0] < start[0] or search[1] < start[1]) and start[0] != 0 and start[1] != 0:
            if start[0] > start[1]:
                start = (start[0] % start[1], start[1])
            else:
                start = (start[0], start[1] % start[0])

        if (search[0] > start[0] and start[1] > 0 and search[0] % start[1] == start[0]):
            start = (search[0], start[1])
        elif (search[1] > start[1] and start[0] > 0 and search[1] % start[0] == start[1]):
            start = (start[0], search[1])

        return search == start