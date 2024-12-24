# https://leetcode.com/problems/redundant-connection/
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []

        visited = set()
        result = []
        adjList = {i:[] for i in range(1, len(edges) + 1)}

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





        