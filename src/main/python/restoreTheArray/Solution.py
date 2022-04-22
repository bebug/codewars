class Solution:
    results = []

    def numberOfArrays(self, s: str, k: int) -> int:
        self.results = [-1 for y in range(len(s) + 1)]
        self.results[len(s)] = 1

        self.recursive(s, 0, k)

        return self.results[0] % (pow(10, 9) + 7)

    def recursive(self, s: str, pos: int, k: int) -> int:
        if self.results[pos] >= 0:
            return self.results[pos]

        solution = 0

        if s[pos] != '0':
            for i in range(pos, len(s)):
                number = int(s[pos:i + 1])

                if number <= 0:
                    continue

                if number > k:
                    break

                solution = solution + self.recursive(s, i + 1, k)
        self.results[pos] = solution
        return solution
