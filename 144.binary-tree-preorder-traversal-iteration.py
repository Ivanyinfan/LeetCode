#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
from utils import TreeNode, list2TreeNode, test
from typing import Optional, List
from collections import deque
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        s, r = deque([root]), list()
        while s:
            node:TreeNode = s.pop()
            r.append(node.val)
            if node.right: s.append(node.right)
            if node.left: s.append(node.left)
        return r
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.preorderTraversal(list2TreeNode([1,None,2,None,None,3,None])), [1,2,3])
    test(sol.preorderTraversal(list2TreeNode([1])),[1])
    test(sol.preorderTraversal(list2TreeNode([1,4,3,2])), [1,4,2,3]) # 53

# Accepted
# 69/69 cases passed (61 ms)
# Your runtime beats 5.36 % of python3 submissions
# Your memory usage beats 73.94 % of python3 submissions (14.2 MB)
