# https://leetcode.com/problems/reconstruct-itinerary/
import heapq
from collections import defaultdict


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 使用 min-heap 來確保字典序
        graph = defaultdict(list)
        for frm, to in tickets:
            heapq.heappush(graph[frm], to)

        route = []

        def visit(airport):
            while graph[airport]:
                next_stop = heapq.heappop(graph[airport])
                visit(next_stop)
            route.append(airport)

        visit("JFK")
        return route[::-1]


# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         # gragh / backtracking
#         # ORD

#         adj = {}
#         tickets.sort()
#         for src, dst in tickets:
#             if src not in adj:
#                 adj[src] = []
#             adj[src].append(dst)

#         res = []
#         res.append('JFK')

#         def dfs(src):
#             if len(res) == len(tickets) + 1:
#                 return True
#             if src not in adj:
#                 return False
#             tmp = list(adj[src])
#             for idx, val in enumerate(tmp):
#                 adj[src].pop(idx)
#                 res.append(val)
#                 if dfs(val):
#                     return True
#                 adj[src].insert(idx, val)
#                 res.pop()
#             return False


#         dfs('JFK')
#         return res
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()
        for src, dst in tickets:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        res = []

        def dfs(airport):
            if airport not in adj:
                res.append(airport)
                return
            while adj[airport]:
                ap = adj[airport].pop(0)
                dfs(ap)
            res.append(airport)

        dfs("JFK")
        res = res[::-1]
        return res
