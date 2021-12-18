#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
from typing import Optional, List
from utils import TreeNode, list2TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [[root, [str(root.val)]]]
        r = list()
        while stack:
            node, path = stack.pop()
            first = True
            if node.left:
                path.append(str(node.left.val))
                stack.append([node.left, path])
                first=False
            if node.right:
                if first:
                    path.append(str(node.right.val))
                else:
                    path = path.copy()
                    path[-1]=str(node.right.val)
                stack.append([node.right, path])
                first=False
            if first:
                r.append(path)
        for i, re in enumerate(r): r[i]='->'.join(re)
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.binaryTreePaths(list2TreeNode([1,2,3,None,5])),["1->2->5","1->3"],False)
    test(sol.binaryTreePaths(list2TreeNode([1,2,3,4,5])),["1->2->4","1->2->5","1->3"],False)
    test(sol.binaryTreePaths(list2TreeNode([1])),["1"],False)

# Accepted
# 208/208 cases passed (37 ms)
# Your runtime beats 22.49 % of python3 submissions
# Your memory usage beats 30 % of python3 submissions (14.4 MB)
