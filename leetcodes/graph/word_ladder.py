# https://leetcode.com/problems/word-ladder/
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordDict = {}
        for word in wordList:
            for i in range(len(word)):
                newWord = word[:i] + "*" + word[i + 1 :]
                if newWord not in wordDict:
                    wordDict[newWord] = []
                wordDict[newWord].append(word)

        print(wordDict)
        visited = set()
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)
        level = 1

        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level
                for k in range(len(word)):
                    pattern = word[:k] + "*" + word[k + 1 :]
                    if pattern not in wordDict:
                        continue
                    for nei in wordDict[pattern]:
                        if nei in visited:
                            continue
                        q.append(nei)
                        visited.add(nei)
            level += 1
        return 0
