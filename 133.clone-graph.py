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
        root = Node(node.val, [None]*len(node.neighbors))
        visited = {root.val: root}
        stack = [[node, 0]]
        while stack:
            if stack[-1][1]==len(stack[-1][0].neighbors):
                stack.pop()
                continue
            node: Node = stack[-1][0]
            for i in range(stack[-1][1], len(node.neighbors)):
                neighbour_i = node.neighbors[i]
                val = neighbour_i.val
                if val not in visited:
                    copy = Node(val, [None]*len(neighbour_i.neighbors))
                    visited[val] = copy
                    stack[-1][1] = i+1
                    visited[node.val].neighbors[i] = visited[val]
                    stack.append([neighbour_i,0])
                    break
                visited[node.val].neighbors[i] = visited[val]
                stack[-1][1] = i+1
        return root


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors.append(node_2)
    node_1.neighbors.append(node_4)
    node_2.neighbors.append(node_1)
    node_2.neighbors.append(node_3)
    node_3.neighbors.append(node_2)
    node_3.neighbors.append(node_4)
    node_4.neighbors.append(node_3)
    node_4.neighbors.append(node_1)
    sol.cloneGraph(node_1)

# Accepted
# 22/22 cases passed (63 ms)
# Your runtime beats 8.98 % of python3 submissions
# Your memory usage beats 60.23 % of python3 submissions (14.6 MB)
