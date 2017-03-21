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
            # curr word ends here
            node.counter += 1


    def getNumWords(self):
        return self.counter

    def dump(self, stringBuilder):
        if self.getNumWords():
            # prints the word and occurrences
            print "%d times for %s" % (self.getNumWords(), ''.join(stringBuilder))
        for letter in sorted(self.children):
            stringBuilder.append(letter)
            self.children[letter].dump(stringBuilder)
            stringBuilder.pop()

class Trie:
    def __init__(self):
        self.nodes = {}

    def addWord(self, word):
        if len(word) == 0:
            return
        print "adding %s" % (word)
        try:
            node = self.nodes[word[0]]
        except KeyError:
            node = TrieNode()
            self.nodes[word[0]] = node
        if len(word) > 1:
            node.addLetter(word, 1)
        else:
            node.counter += 1

    def removeWord(self, word):
        pass


    def dump(self):
        stringBuilder = []
        for letter in sorted(self.nodes):
            stringBuilder.append(letter)
            node = self.nodes[letter].dump(stringBuilder)
            stringBuilder.pop()

myTrie = Trie()
myTrie.addWord('a')
myTrie.addWord('a')
myTrie.addWord('a')
myTrie.addWord('estro')
myTrie.addWord('estro')
myTrie.addWord('estroso')
myTrie.addWord('any')
myTrie.addWord('anything')
myTrie.addWord('ab')
myTrie.addWord('est')
myTrie.dump()

