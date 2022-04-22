class Solution:
    def frequencySort(self, s: str) -> str:
        characters = {}
        for char in s:
            if char in characters:
                characters[char] = characters[char] + 1
            else:
                characters[char] = 1

        output = ''
        for w in sorted(characters.items(), key=lambda kv: kv[1], reverse=True):
            output = output + w[0]*w[1]

        return output