class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        map = [False]*(len(s)+1)
        for i in range(len(map)):
            map[i] = [False] * (len(p) + 1)
        map[0][0] = True

        for i in range(1, len(p)+1):
            if p[i-1] == "*":
                map[0][i] = map[0][i-1]
            else:
                map[0][i] = False

        for i in range(1, len(s)+1):
            map[i][0] = False

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                char = s[i-1]
                pattern = p[j-1]

                if pattern == "*":
                    map[i][j] = map[i-1][j] or map[i][j-1]
                if pattern == char or pattern == "?":
                    map[i][j] = map[i-1][j-1]

        return map[len(s)][len(p)]






