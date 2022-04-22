
class Solution:
    """ A Python3 program to answer queries to check whether
the substrings are palindrome or not efficiently """
    NO_OF_CHARS = 26

    def computeTransFun(self, pat, M, TF):

        lps = 0

        # Fill entries in first row
        for x in range(self.NO_OF_CHARS):
            TF[0][x] = 0
        TF[0][ord(pat[0])-ord('a')] = 1

        # Fill entries in other rows
        for i in range(1, M+1):

            # Copy values from row at index lps
            for x in range(self.NO_OF_CHARS):
                TF[i][x] = TF[lps][x]

            if (i < M):
                # Update the entry corresponding to this character
                TF[i][ord(pat[i])-ord('a')] = i + 1

                # Update lps for next row to be filled

                lps = TF[lps][ord(pat[i])-ord('a')]

        # Prints all occurrences of pat in txt


    def search(self,pat, txt):
        M = len(pat)
        N = len(txt)
        TF = [[0 for i in range(self.NO_OF_CHARS)] for j in range(M + 1)]
        self.computeTransFun(pat, M, TF)

        # process text over FA.
        j = 0
        for i in range(N):
            j = TF[j][ord(txt[i])]
            if (j == M):
                print("pattern found at index", i - M + 1)
