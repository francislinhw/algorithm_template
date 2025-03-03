# https://leetcode.com/problems/implement-trie-prefix-tree/


# 1 March 2025 Practice
class Trie:
    def __init__(self):
        # 1020
        """
        Initialize your data structure here.
        """
        self.wordMap = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        thisDict = self.wordMap

        for i in range(len(word)):
            if word[i] not in thisDict:
                thisDict[word[i]] = [{}, False]  # next dict and is the end or not
            if i == len(word) - 1:
                thisDict[word[i]][1] = True
            thisDict = thisDict[word[i]][0]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        thisDict = self.wordMap
        result = False
        for i in word:
            if i not in thisDict:
                return False
            result = thisDict[i][1]
            thisDict = thisDict[i][0]

        return result

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        thisDict = self.wordMap
        for i in prefix:
            if i not in thisDict:
                return False
            thisDict = thisDict[i][0]

        return True

    # 1035 15 min


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_of_word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
