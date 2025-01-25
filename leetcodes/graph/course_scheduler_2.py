# https://leetcode.com/problems/course-schedule-ii/
from typing import List


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
