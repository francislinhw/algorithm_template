# https://leetcode.com/problems/min-cost-to-connect-all-points/
from collections import heapq
from typing import List

import heapq


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def distance(x1, x2, y1, y2):
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            total_cost += cost

            # 將所有未訪問過的點加入 heap
            for j in range(n):
                if j not in visited:
                    dist = distance(
                        points[i][0], points[j][0], points[i][1], points[j][1]
                    )
                    heapq.heappush(min_heap, (dist, j))

        return total_cost


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Link all points
        # Heap to store all values to points
        # To prevent backward

        # def manhattanDistance(p1, p2):
        #     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # n = len(points)
        # visited = set()
        # minHeap = [(0, 0)]  # (cost, point_index)
        # totalCost = 0

        # while len(visited) < n:
        #     cost, curr = heapq.heappop(minHeap)
        #     if curr in visited:
        #         continue
        #     visited.add(curr)
        #     totalCost += cost

        #     for next_point in range(n):
        #         if next_point not in visited:
        #             dist = manhattanDistance(points[curr], points[next_point])
        #             heapq.heappush(minHeap, (dist, next_point))

        # return totalCost
        def manhattanDistance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        distanceMap = {}
        for i in range(n):
            distanceMap[i] = []
        # 建立鄰接表
        for i in range(n):
            for j in range(i + 1, n):  # 避免重複建雙向邊
                dist = manhattanDistance(points[i], points[j])
                distanceMap.setdefault(i, []).append((dist, j))
                distanceMap.setdefault(j, []).append((dist, i))

        # Prim's Algorithm: 使用 heap 擴展最小生成樹
        visited = set()
        minHeap = [(0, 0)]  # (cost, from_point_index)
        totalCost = 0

        while len(visited) < n:
            cost, curr = heapq.heappop(minHeap)
            if curr in visited:
                continue
            visited.add(curr)
            totalCost += cost

            for edgeCost, neighbor in distanceMap[curr]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (edgeCost, neighbor))

        return totalCost  # Add edge from the smallest to the largest until all points are visited


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim Algorithem (greedy algorithm)
        # this algo = heap + bfs
        # MST (Minimum Spanning Tree) algorithm
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visited = set()
        minH = [[0, 0]]
        heapq.heapify(minH)

        while len(visited) < N:
            cost, i = heapq.heappop(minH)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minH, [neiCost, nei])
        return res
