# https://leetcode.com/problems/graph-valid-tree/ (Subscription required)
# https://neetcode.io/problems/valid-tree
from typing import (
    List,
)

from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # # write your code here
        # if n - 1 != edges:
        #     return False

        # if not n or not edges:
        #     return False

        # visited = set()

        # adjacencyMap = {i:[] for i in range(n)}

        # for node, edge in edges:
        #     adjacencyMap[node].append(edge)
        #     adjacencyMap[edge].append(node)

        # # Tree = edge = n - 1 (or graph) and node = node
        # q = dque()
        # q.append(adjacencyMap[0])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         visited.add(node)
        #         otherNodes = adjacencyMap[node]
        #         for n in otherNodes:
        #             if n in visited:
        #                 continue
        #             q.append(n)

        # lenthVisited = len(visited)

        # if lenthVisited == n:
        #     return True

        # return False

        # write your code here

        if n - 1 != len(edges):
            return False

        adjList = {i: [] for i in range(n)}
        visited = set()
        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)

        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                for i in range(len(q)):
                    n = q.popleft()
                    visited.add(n)
                    for child in adjList[n]:
                        if child not in visited:
                            q.append(child)

        bfs(0)
        # For tree, the number of nodes is equal to the number of edge + 1
        return True if len(visited) == n else False


# Dfs
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False

        if not edges:
            return True

        # edge case remember
        if n - 1 != len(edges):
            return False

        adjList = {_: [] for _ in range(n)}

        visited = set()

        print(adjList)

        for edge in edges:
            s, e = edge
            adjList[s].append(e)
            adjList[e].append(s)

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for subnode in adjList[node]:
                dfs(subnode)

        dfs(0)

        print(visited)

        return True if len(visited) == n else False
