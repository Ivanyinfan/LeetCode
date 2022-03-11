
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        diameter = 0
        def dfs(node: Node):
            nonlocal diameter
            if not node.children:
                return 0
            first = second = 0
            for child in node.children:
                r = dfs(child) + 1
                if r>=first:
                    first, second = r, first
                elif r>second:
                    second = r
            diameter = max(first+second, diameter)
            return first
        dfs(root)
        return diameter

from utils import test
if __name__ == "__main__":
    sol = Solution()
    node = Node()
    test(sol.diameter(node), 0)
    node = Node(0,[Node()])
    test(sol.diameter(node), 1)