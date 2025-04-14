# https://leetcode.com/problems/network-delay-time/description/
from collections import heapq
from typing import List
from collections import defaultdict


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # 10.56
        # Overview
        # 1. BFS: start k, iterate layer by layer, traversed set, len(set) != n -> -1 or return time
        # variable to record min time

        # Step 1:

        # adjMap = {}

        # for s, t, time in times:
        #     if s not in adjMap:
        #         adjMap[s] = []
        #     adjMap[s].append([t, time])

        # queue = deque()
        # queue.append(k)
        # visited = set()

        # minTime = 0

        # while queue:
        #     maxValueThisRound = 0
        #     for _ in range(len(queue)):
        #         element = queue.popleft()
        #         visited.add(element)
        #         if len(visited) == n:
        #             break
        #         if element in adjMap:
        #             for nextElement, timeValue in adjMap[element]:
        #                 maxValueThisRound = max(maxValueThisRound, timeValue)
        #                 if nextElement in adjMap and nextElement not in visited:
        #                     queue.append(nextElement)
        #                 elif nextElement not in visited:
        #                     visited.add(nextElement)

        #     minTime += maxValueThisRound

        # if len(visited) < n:
        #     return -1

        # return minTime
        # 建立鄰接表
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 最小堆：[(當前總時間, 當前節點)]
        heap = [(0, k)]
        # 記錄每個節點的最小到達時間
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, t in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + t, nei))

        if len(dist) < n:
            return -1
        return max(dist.values())


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
