
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        field = [[0 for x in range(n + 1)] for y in range(m + 1)]
        field[1][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                field[i][j] = field[i-1][j] + field[i][j-1]

        return field[m][n]