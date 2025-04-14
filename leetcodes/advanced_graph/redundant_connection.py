# https://leetcode.com/problems/redundant-connection/
from typing import List


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
