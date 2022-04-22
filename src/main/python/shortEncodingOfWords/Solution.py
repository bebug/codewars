from typing import List

class Node:

    def __init__(self):
        self.childNodes = {}
        self.hit = False
        self.word = ""

    def build(self, word: str, index):
        if -1 < index:
            character = word[index]
            if character not in self.childNodes:
                self.childNodes[character] = Node()
            self.childNodes[character].build(word, index - 1)
        else:
            self.hit = True
            self.word = word

    def __repr__(self):
        return str(self.word) + "=" + str(self.childNodes)



class Solution:
    def traverse(self, root: Node, words: List):
        if not root:
            return
        if len(root.childNodes) <= 0:
            words.append(root.word)
        else:
            for node in root.childNodes:
                self.traverse(root.childNodes[node], words)


    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = Node()
        for word in words:
            root.build(word, len(word) -1)
        wordList = []
        self.traverse(root, wordList)
        length = len(wordList)
        for word in wordList:
            length = length + len(word)

        return length


