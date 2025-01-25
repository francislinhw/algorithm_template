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

        # Practice DFS Approach - Got error

    def ladderLength_2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def wordDistance(word1, word2) -> int:
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1

            return diff

        wordList.append(beginWord)

        adjList = {word: [] for word in wordList}

        for word1 in wordList:
            for word2 in wordList:
                distance = wordDistance(word1, word2)
                if distance == 1:
                    adjList[word1].append(word2)

        visited = set()
        global result
        result = float("inf")

        def dfs(word, target, layer):
            print("Word: ", word)
            if word == target:
                layer += 1
                global result
                result = min(layer, result)
                print("result", result)
                return True, layer
            if word in visited:
                return False, 0
            visited.add(word)
            layer += 1

            for adjWord in adjList[word]:
                dfs(adjWord, target, layer)

        dfs(beginWord, endWord, 0)

        return result if result != float("inf") else 0
