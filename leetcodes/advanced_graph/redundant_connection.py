# https://leetcode.com/problems/redundant-connection/
from typing import List

from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # x and y are already connected

            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                if rank[rootX] == rank[rootY]:
                    rank[rootX] += 1
            return True  # <-- 確保不管哪個分支都有 return

        for u, v in edges:
            if not union(u, v):
                return [u, v]


class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # x and y are already connected

            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                if rank[rootX] == rank[rootY]:
                    rank[rootX] += 1
                return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]


class Solution(object):
    def findRedundantConnection(self, edges):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):
                return [u, v]


class Solution(object):
    def findRedundantConnection(self, edges):
        graph = defaultdict(list)

        def dfs(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in graph[source]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        for u, v in edges:
            visited = set()
            if u in graph and v in graph and dfs(u, v, visited):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)


class Solution(object):
    def findRedundantConnection(self, edges):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # 路徑壓縮
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # 已經在同一集合 -> 會形成環
            parent[rootY] = rootX
            return True

        for u, v in edges:
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if not union(u, v):
                return [u, v]

        # # 10.48

        # # step 1: for loop edges to be ignore
        # # step 2: check if ignored edges is legal to form the original graph (# of nodes)
        # res = []

        # def dfs(node, adjList):
        #     if len(visited) == len(edges):
        #         return True
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     isConnected = False
        #     for n in adjList[node]:
        #         result = dfs(n, adjList)
        #         isConnected = result or isConnected

        #     return isConnected

        # redundant = []

        # for ignoreEdge in edges:
        #     visited = set()
        #     adjMap = {}
        #     for i in range(1, len(edges) + 1):
        #         adjMap[i] = []
        #     for f, t in edges:
        #         if [f, t] != ignoreEdge:
        #             adjMap[f].append(t)
        #             adjMap[t].append(f)

        #     isOkay = dfs(1, adjMap)

        #     if isOkay:
        #         redundant.append(ignoreEdge)

        # return redundant[-1] # 11.14 26 mins


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 10.48

        # step 1: for loop edges to be ignore
        # step 2: check if ignored edges is legal to form the original graph (# of nodes)
        res = []

        def dfs(node, adjList):
            if len(visited) == len(edges):
                return True
            if node in visited:
                return False
            visited.add(node)
            isConnected = False
            for n in adjList[node]:
                result = dfs(n, adjList)
                isConnected = result or isConnected

            return isConnected

        redundant = []

        for ignoreEdge in edges:
            visited = set()
            adjMap = {}
            for i in range(1, len(edges) + 1):
                adjMap[i] = []
            for f, t in edges:
                if [f, t] != ignoreEdge:
                    adjMap[f].append(t)
                    adjMap[t].append(f)

            isOkay = dfs(1, adjMap)

            if isOkay:
                redundant.append(ignoreEdge)

        return redundant[-1]  # 11.14 26 mins


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        visited = set()
        result = []
        adjList = {i: [] for i in range(1, len(edges) + 1)}

        for edge in edges:
            nodeOne, nodeTwo = edge
            adjList[nodeOne].append(nodeTwo)
            adjList[nodeTwo].append(nodeOne)

        print(adjList)

        def dfs(preNode: int, node: int):
            if node in visited and node != preNode:
                return True

            visited.add(node)

            adjNodes = adjList[node]

            for adjNode in adjNodes:
                if dfs(node, adjNode):
                    result.append([node, adjNode])

            return False

        dfs(0, 1)
        result.sort()
        print(result)

        # for edge in edges:
        #     nodeOne = edge[0]
        #     nodeTwo = edge[1]

        #     if nodeOne in visited and nodeTwo in visited:
        #         result = [nodeOne, nodeTwo]

        #     visited.add(nodeOne)
        #     visited.add(nodeTwo)

        return result[0]
