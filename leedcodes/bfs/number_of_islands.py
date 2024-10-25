from collections import deque

class Solution:
    def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            visited = set()
            rows = len(grid)
            cols = len(grid[0])
            count = 0

            def dfs(r, c):
                if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or (r, c) in visited:
                    return False
                
                visited.add((r, c))
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)

                return True

            for r in range(rows):
                for c in range(cols):
                    if (r, c) in visited or grid[r][c] == '0':
                        continue
                    if dfs(r, c):
                        count += 1
            return count

# example
input = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

expected_output = 1

s = Solution()
print(s.numIslands(input) == expected_output)