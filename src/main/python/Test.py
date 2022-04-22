
class Node:

    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""

    def addWord(self, word, index):
        if len(word) <= index:
            self.end = True
            self.word = word
            return
        char = word[index]
        if not char in self.children:
            self.children[char] = Node()
        self.children[char].addWord(word, index + 1)

    def __repr__(self) -> str:
        return "Node children:" + str(self.children) + " end:" + str(self.end) + " word:" + str(self.word) + "\n"


class Tree:

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        self.root.addWord(word, 0)

    def __repr__(self) -> str:
        return "Tree: \n" + str(self.root)

tree = Tree()

tree.addWord("hallo")

print(tree)