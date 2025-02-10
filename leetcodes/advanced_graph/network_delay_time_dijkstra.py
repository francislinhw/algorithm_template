# https://leetcode.com/problems/network-delay-time/description/
from collections import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's algo
        # Directed
        adjList = {n: [] for n in range(1, n + 1)}
        for start, end, time in times:
            adjList[start].append(
                (time, end)
            )  # by default use first element to sort in heap

        print(adjList)

        time = 0
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        visited = set()

        while minHeap:
            time1, destination = heapq.heappop(minHeap)
            if destination in visited:
                continue
            visited.add(destination)
            time = max(time, time1)  #
            for time2, dest in adjList[destination]:
                if dest in visited:
                    continue

                heapq.heappush(minHeap, (time1 + time2, dest))
        return time if len(visited) == n else -1
