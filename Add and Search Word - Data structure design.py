class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.dic['End'] = False

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.dic
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
            if 'End' not in root: root['End'] = False
        root['End'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.dic
        def helper(word,nodes):
            for i in range(len(word)):
                if word[i] == '.':
                    for node in nodes:
                        if node!='End' and helper(word[i+1:], nodes[node]):
                            return True
                    return False
                elif word[i] not in nodes:
                    return False
                nodes = nodes[word[i]]
            return nodes['End']
        return helper(word, root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
