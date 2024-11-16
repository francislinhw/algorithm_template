from typing import (
    List,
)


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
