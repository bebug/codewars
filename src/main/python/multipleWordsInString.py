
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
        return str(self.children) + (self.word if self.end else "")


class Tree:

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        self.root.addWord(word, 0)

    def __repr__(self) -> str:
        return "Tree: \n" + str(self.root)

tree = Tree()

tree.addWord("hallo")
tree.addWord("hallu")
tree.addWord("hollu")

text = "jafdsljfkhallofjdklfsdafholludsafs"

def addWords(text, index, found):
    print(text, index)
    node = tree.root
    while index < len(text) -1:
        if node.end:
            found.append(node.word)
        if text[index] in node.children:
            node = node.children[text[index]]
        else:
            return
        index = index+1

found = []
for i in range(len(text)):
    addWords(text, i, found)

print(found)