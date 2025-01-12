# https://www.lintcode.com/problem/892/description
# hard -> memorize
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:        
        adjList = {}
        for word in words:
            for char in word:
                if char not in adjList:
                    adjList[char] = set()
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        path = set()
        added = set()
        res = []
        
        def dfs(char):
            if char in path:
                return True
            if char in added:
                return False
            path.add(char)
            added.add(char)
            for nei in adjList[char]:
                if dfs(nei):
                    return True
            path.remove(char)
            res.append(char)
            return False
        
        for c in adjList:
            if dfs(c):
                return ''
        res.reverse()
        return ''.join(res)