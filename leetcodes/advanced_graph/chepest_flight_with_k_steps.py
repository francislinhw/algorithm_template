# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

from typing import List
from collections import deque
import heapq
from collections import defaultdict

# from typing import List

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         # 建立鄰接表與價格表
#         adjDict = {}
#         priceDict = {}

#         for f, t, p in flights:
#             if f not in adjDict:
#                 adjDict[f] = []
#             adjDict[f].append(t)
#             priceDict[(f, t)] = p

#         # 初始價格表
#         container = {i: float("inf") for i in range(n)}
#         container[src] = 0

#         # 最多 k+1 條邊
#         for _ in range(k + 1):
#             # 這一輪的暫存價格表
#             new_container = container.copy()
#             for f, t, p in flights:
#                 if container[f] != float("inf"):
#                     new_container[t] = min(new_container[t], container[f] + p)
#             container = new_container

#         return -1 if container[dst] == float("inf") else container[dst]


from typing import List
from collections import deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # 建立鄰接表 {f: [(t, p), ...]}
        adjDict = {}
        for f, t, p in flights:
            if f not in adjDict:
                adjDict[f] = []
            adjDict[f].append((t, p))

        # 價格初始化
        prices = [float("inf")] * n
        prices[src] = 0

        # BFS queue: (目前城市, 總價)
        q = deque([(src, 0)])
        stops = 0

        # 最多走 k+1 層
        while q and stops <= k:
            size = len(q)
            # 暫存這一層的更新，避免同層相互影響
            new_prices = prices[:]
            for _ in range(size):
                city, cost = q.popleft()
                if city not in adjDict:
                    continue
                for nei, price in adjDict[city]:
                    if cost + price < new_prices[nei]:
                        new_prices[nei] = cost + price
                        q.append((nei, cost + price))
            prices = new_prices
            stops += 1

        return -1 if prices[dst] == float("inf") else prices[dst]


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # (累積價格, 當前城市, 已轉機次數)
        heap = [(0, src, 0)]
        # 到達 (城市, stops) 時的最小 cost
        best = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost
            if stops > k:
                continue

            # 如果以前到過這個城市在這個 stops 次數內，而且更便宜 → 跳過
            if (city, stops) in best and best[(city, stops)] <= cost:
                continue

            best[(city, stops)] = cost

            for nei, price in graph[city]:
                heapq.heappush(heap, (cost + price, nei, stops + 1))

        return -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # prices = [float('inf')] * n
        # prices[src] = 0

        # for i in range(k+1):
        #     tmp = prices.copy()
        #     for s, d, p in flights:
        #         # If the node is inf, then it means there are no path has reached that node yet.
        #         if prices[s] == float('inf'):
        #             continue
        #         # If the new path smaller then that previous val, smaller than tmp[d] instead of prices[d]
        #         # because during the loop, tmp[d] might be updated by other nodes which might gives different val
        #         if prices[s] + p < tmp[d]:
        #             tmp[d] = prices[s] + p
        #     prices = tmp
        # return prices[dst] if prices[dst] != float('inf') else -1
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        q = deque([(0, src, 0)])
        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue

            for nei, w in adj[node]:
                nextCost = cst + w
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops + 1))

        return prices[dst] if prices[dst] != float("inf") else -1
