# https://neetcode.io/problems/count-connected-components
from typing import (
    List,
)


# 15 March 2025 Practice
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 2.04

        # Step 1: adjList

        # Step 2: DFS to iterate the adjList # exit: all components linked
        # Step 3: Variable to count how many DFS to run to visit all nodes
        # Step 4: Return Count
        if n == 1:
            return 1
        if not edges:
            return n

        adjMap = {}

        # init of Map
        for i in range(n + 1):
            adjMap[i] = []

        for start, end in edges:
            adjMap[start].append(end)
            adjMap[end].append(start)

        # Map = {1: [2, 3]}
        visited = set()

        def dfs(node: int):
            if node in visited:
                return False  # already have this
            if node not in visited:
                visited.add(node)
            for vertix in adjMap[node]:
                dfs(vertix)
            return True

        cnt = 0
        for i in range(0, n, 1):
            decision = dfs(i)
            if decision:
                cnt += 1

        return cnt  # 2.23 19 mins


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here

        visited = set()  # Adjancency list

        undirectedMap = {}
        undirectedMap = {i: [] for i in range(n)}
        for listL in edges:
            nodeOne = listL[0]
            nodeTwo = listL[1]
            undirectedMap[nodeOne].append(nodeTwo)
            undirectedMap[nodeTwo].append(nodeOne)

        numbersOfConnectedComponent = 0

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for nextNode in undirectedMap[node]:
                dfs(nextNode)

            return True

        for i in range(n):
            if i in visited:
                continue
            if dfs(i):  # Run every node
                numbersOfConnectedComponent += 1

        return numbersOfConnectedComponent
