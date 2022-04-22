class Node {
    children = [];

    addWord(word, index) {
        console.log(word)
        console.log(index)
        if (word.length <= index) {
            console.log("hit");
            this.hit = true;
            this.word = word;
            return
        }
        let currentChar = word.charAt(index);
        console.log(currentChar)
        if (!this.children[currentChar]) {
            this.children[currentChar] = new Node()
        }
        this.children[currentChar].addWord(word, index + 1)
    }
}

const root = new Node()
root.addWord("hallo", 0);
root.addWord("hullo", 0);
const text = "hallohullofjasfkldsajhallofjsdakflsdjhulloasdfsda"

console.log(JSON.stringify(root))

let isIn = function(text, index, hits) {
    let currentNode = root;

    while(index < text.length) {
        if (!currentNode) {
            return;
        }
        const currentChar = text[index];
        if (currentNode.hit) {
            hits.add(currentNode.word)
        }
        if (currentNode.children[currentChar]) {
            currentNode = currentNode.children[currentChar];
        }
        else {
            currentNode = null;
        }
        index++;
    }
}

var hits = new Set()
for (var i = 0; i < text.length; i++) {
    isIn(text, i, hits)
}

console.log(hits)