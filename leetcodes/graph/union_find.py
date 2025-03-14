# https://leetcode.com/problems/redundant-connection/description/
from typing import List


# Minimize Version (Omit Rank)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [n for n in range(len(edges) + 1)]

        def find(n):
            p = par[n]  # 先找到當前節點 n 的父節點
            while p != par[p]:  # 當前節點的父節點還不是它自己，表示還沒找到根
                par[p] = par[par[p]]  # 路徑壓縮：把當前節點的父節點指向「祖父節點」
                p = par[p]  # 繼續向上找根節點
            return p  # 回傳根節點

        def union(n1, n2):
            p1 = find(n1)  # 找到 n1 的根節點
            p2 = find(n2)  # 找到 n2 的根節點

            if p1 == p2:
                return True  # 形成環
            par[p2] = p1  # 把 p2 併入 p1, rank 不變, 效能較差
            return False  # 尚未形成環

        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [
            n for n in range(len(edges) + 1)
        ]  # 初始化每個節點的父節點為自己 # e.g. par[1] = 1, par[2] = 2, par[3] = 3
        rank = [
            1 for n in range(len(edges) + 1)
        ]  # 初始化每個節點的秩為1, 用來記錄每個節點的子樹大小, e.g. rand[1] = 1 表示節點1的子樹大小為1

        def find(n):
            p = par[
                n
            ]  # 先找到當前節點 n 的父節點. e.g. par[1] = 1, 初始化時每個節點的父節點都是自己
            while (
                p != par[p]
            ):  # 當前節點的父節點還不是它自己，表示還沒找到根, 什麼時候 p != par[p] 呢? 由於初始化時每個節點的父節點都是自己的位置, 所以 p != par[p] 的時候就是還沒找到根節點的時候
                par[p] = par[par[p]]  # 路徑壓縮：把當前節點的父節點指向「祖父節點」
                p = par[p]  # 繼續向上找根節點
            return p  # 回傳根節點

        def union(n1, n2):
            p1 = find(n1)  # 找到 n1 的根節點
            p2 = find(n2)  # 找到 n2 的根節點

            if p1 == p2:
                return True  # 代表 n1 和 n2 已經在同一個集合中，合併會形成環 (cycle)，所以返回 True

            # 若 p1 和 p2 不在同一個集合中, 表示兩者屬於不同的子樹, 所以需要合併, 合併的邏輯為
            # 1. 比較兩者子樹的大小, 把較小的子樹併入較大的子樹
            # 2. 如果兩者子樹大小相同, 則把 p2 併入 p1, 並且 p1 的秩加1
            if rank[p1] > rank[p2]:  # 如果 p1 所在的集合比較大
                par[p2] = p1  # 把 p2 併入 p1
                rank[p1] += rank[p2]  # 更新 p1 的秩
            else:  # 如果 p2 的集合較大，或兩者相等
                par[p1] = p2  # 把 p1 併入 p2
                rank[p2] += rank[p1]  # 更新 p2 的秩
            return False  # 成功合併, 但還沒有形成環

        for n1, n2 in edges:  # 遍歷所有邊
            if union(n1, n2):  # 形成環
                return [n1, n2]  # 返回該邊


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [n for n in range(len(edges) + 1)]
        rank = [1 for n in range(len(edges) + 1)]

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
