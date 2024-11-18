# https://leetcode.com/problems/reconstruct-itinerary/
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
