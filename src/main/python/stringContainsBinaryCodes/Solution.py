class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        myset = set()

        for i in range(0, len(s) -k + 1):
            substr = s[i:i+k]
            myset.add(int(substr, 2))
            if len(myset) == need:
                return True

        return False
