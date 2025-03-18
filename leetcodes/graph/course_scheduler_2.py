# https://leetcode.com/problems/course-schedule-ii/
from typing import List


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 12.47
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        for cus, pre in prerequisites:
            adjList[pre].append(cus)

        visited = set()
        finished = set()
        result = []

        def backtracking(crs):
            if crs in visited:
                return False
            if crs in finished:
                return True
            visited.add(crs)

            for c in adjList[crs]:
                valid = backtracking(c)
                if not valid:
                    return False
            visited.remove(crs)
            result.append(crs)
            finished.add(crs)

            return True

        for i in range(numCourses):
            dicision = backtracking(i)
            if not dicision:
                return []

        return result[::-1]


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {crs: [] for crs in range(numCourses)}
        visiting = set()
        result = []
        done = set()
        for crs, preq in prerequisites:
            preMap[crs].append(preq)

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in done:
                return True
            visiting.add(crs)
            for preq in preMap[crs]:
                valid = dfs(preq)
                if not valid:
                    return False
            visiting.remove(crs)
            done.add(crs)
            result.append(crs)
            return True

        for crs in preMap:
            if not dfs(crs):
                return []
        return result
