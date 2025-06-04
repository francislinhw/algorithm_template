# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjMap = {}  # course -> list of prereqs
        for course, pre in prerequisites:
            if course not in adjMap:
                adjMap[course] = []
            adjMap[course].append(pre)

        visited = [0] * numCourses  # 0=未拜訪, 1=拜訪中, 2=拜訪結束

        def hasCycle(course):
            if visited[course] == 1:
                return True  # 發現環
            if visited[course] == 2:
                return False  # 已經檢查過，沒問題
            visited[course] = 1  # 標記為拜訪中
            for pre in adjMap.get(course, []):
                if hasCycle(pre):
                    return True
            visited[course] = 2  # 標記為拜訪結束
            return False

        for course in range(numCourses):
            if hasCycle(course):
                return False  # 有環
        return True  # 沒環，可以修完所有課程


class Solution:
    def canFinish(self, numCourses, prerequisites):
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
