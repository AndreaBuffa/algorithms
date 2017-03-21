class TrieNode:
    def __init__(self):
        self.counter = 0 #num of words ending at this node
        self.partialCounter = 0 #num of words sharing this node
        self.children = {}

    def addLetter(self, word, index):
        try:
            node = self.children[word[index]]
        except KeyError:
            node = TrieNode()
            self.children[word[index]] = node
        index += 1
        if index < len(word):
            self.partialCounter += 1
            node.addLetter(word, index)
        else:
            self.counter += 1

    def hasChild(self):
        return

    def getNumWords(self):
        return self.counter

class Trie:
    def __init__(self):
        self.nodes = {}

    def addWord(self, word):
        if len(word) == 0:
            return
        try:
            node = self.nodes[word[0]]
        except KeyError:
            node = TrieNode()
            self.nodes[word[0]] = node
        if len(word) > 1
            node.addLetter(word, 1)
        else:
            node.counter += 1

    def removeWord(self, word):
        pass


    def dump(self):
        stringBuilder  = []
        for letter in sorted(self.nodes):
            node = self.nodes[letter]
            if node.getNumWords():
                print "%s %d" % (letter, node.getNumWords())
            if node.hasChild()
                stringBuilder
                node.dump(stringBuilder)

        for letter, node in self.nodes.items:
            #for node.co




