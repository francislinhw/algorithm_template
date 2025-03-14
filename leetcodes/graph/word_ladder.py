# https://leetcode.com/problems/word-ladder/
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 2.36
        # BFS: map from word to words
        # BFS cnt += 1
        # 將 wordList 轉換為 set 以加速查找
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0  # 目標單詞不在字典內，不可能轉換成功

        def countWordDiff(word1, word2) -> int:
            return sum(1 for i in range(len(word1)) if word1[i] != word2[i])

        # 建立 BFS queue
        queue = deque([(beginWord, 1)])  # (當前字, BFS 層數)
        visited = set()

        while queue:
            currentWord, layer = queue.popleft()

            if currentWord == endWord:
                return layer  # 找到 endWord，返回步數

            for i in range(len(currentWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = currentWord[:i] + c + currentWord[i + 1 :]
                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, layer + 1))

        return 0  # 無法轉換


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 2.36
        # BFS: map from word to words
        # BFS cnt += 1
        wordList.append(beginWord)

        def countWordDiff(word1, word2) -> int:
            cnt = 0
            for i in range(len(word1)):
                char = word1[i]
                if char != word2[i]:
                    cnt += 1
            return cnt

        wordHashMap = {}

        for word in wordList:
            wordHashMap[word] = []

        for key, content in wordHashMap.items():
            for word in wordList:
                if countWordDiff(key, word) == 1:
                    content.append(word)

        visited = set()
        queue = deque([[beginWord]])
        layer = 1

        while queue != []:
            currentWords = queue.popleft()
            layer += 1
            newList = []
            for word in currentWords:
                visited.add(word)

                for nextWord in wordHashMap[word]:
                    if nextWord == endWord:
                        return layer
                    else:
                        if nextWord not in visited:
                            newList.append(nextWord)
            if newList != []:
                queue.append(newList)
            else:
                return 0

        return layer


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
