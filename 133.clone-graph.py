#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        root = Node(node.val)
        visited = {root.val: root}
        stack = [[node, 0]]
        while stack:
            if stack[-1][1]==len(stack[-1][0].neighbors):
                stack.pop()
                continue
            for i in range(stack[-1][1], len(stack[-1][0].neighbors)):
                val = stack[-1][0].neighbors[i].val
                if val not in visited:
                    copy = Node(val)
                    visited[val]=copy
                    stack[-1][1] += 1
                    stack.append([stack[-1].neighbors[i],0])
                    break
                else:
                    visited[stack[-1][0].val].neighbors[i] = visited[val]
                    stack[-1][1] = i+1
        return root


# @lc code=end

