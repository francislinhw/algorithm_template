# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list. (dict)
        # Cycle detection
        # (un)directed graph
        # directed with weights
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
                return False
        return True


# done for 不知從哪個點開始
