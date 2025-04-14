# https://www.lintcode.com/problem/892/description
# hard -> memorize
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def alien_order(self, words: List[str]) -> str:
        adjList = defaultdict(
            set
        )  # dict + set means the dictionary of the node and the set of the nodes it points to
        inDegree = defaultdict(int)

        # 初始化所有字母的 inDegree 為 0, inDegree is the number of edges coming into the node
        for word in words:
            for char in word:
                inDegree[char] = 0

        # 構建圖：每對字比較第一個不同字元
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:  # e.g ["abc", "ab"]
                return ""  # 無效字典順序
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adjList[w1[j]]:
                        adjList[w1[j]].add(w2[j])
                        inDegree[w2[j]] += 1
                    break

        # 使用 heapq 來維持最小字典序的 in-degree 0 集合
        heap = [c for c in inDegree if inDegree[c] == 0]
        heapq.heapify(heap)

        res = []
        while heap:
            c = heapq.heappop(heap)
            res.append(c)
            for nei in adjList[c]:
                inDegree[nei] -= 1  # 因為 c 已經被移除, 所以 nei 的 inDegree 要減 1
                if (
                    inDegree[nei] == 0
                ):  # 因為 nei 的 inDegree 為 0 表示除了 c 之外, 沒有其他邊進入 nei, 所以 nei 可以加入 heap, 有inDegree > 1 表示 nei 還有其他邊進入, 無法確認 nei 是否為第一個字母

                    heapq.heappush(heap, nei)

        if len(res) != len(inDegree):
            return ""  # 有環
        return "".join(res)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {}
        for word in words:
            for char in word:
                if char not in adjList:
                    adjList[char] = set()

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
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
                return ""
        res.reverse()
        return "".join(res)
