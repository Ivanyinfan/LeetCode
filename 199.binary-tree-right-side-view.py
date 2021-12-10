#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return list()
        max_level = 0
        stack = [[root, 1]]
        r = list()
        while stack:
            node, level = stack.pop()
            if level>max_level:
                r.append(node.val)
                max_level = level
            if node.left:
                stack.append([node.left, level+1])
            if node.right:
                stack.append([node.right, level+1])
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.rightSideView(list2TreeNode([1,2,3,None,5,None,4])), [1,3,4])
    test(sol.rightSideView(list2TreeNode([1,None,3])), [1,3])
    test(sol.rightSideView(list2TreeNode([1,2,3,None,5,None,4, None, None, None, 6])), [1,3,4,6])
    test(sol.rightSideView(list2TreeNode([1])), [1])
    test(sol.rightSideView(None), [])

# Accepted
# 215/215 cases passed (24 ms)
# Your runtime beats 97.96 % of python3 submissions
# Your memory usage beats 54.84 % of python3 submissions (14.3 MB)
