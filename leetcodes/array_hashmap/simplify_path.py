# https://leetcode.com/problems/simplify-path/


class Solution(object):
    def simplifyPath(self, path):
        parts = path.split("/")
        stack = []

        for part in parts:
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)
