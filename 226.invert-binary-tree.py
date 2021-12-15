#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
from typing import Optional
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return root
# @lc code=end
from utils import test, list2TreeNode, treeNode2List
if __name__ == "__main__":
    sol = Solution()
    test(treeNode2List(sol.invertTree(list2TreeNode([4,2,7,1,3,6,9]))),[4,7,2,9,6,3,1])
    test(treeNode2List(sol.invertTree(list2TreeNode([2,1,3]))),[2,3,1])
    test(treeNode2List(sol.invertTree(list2TreeNode([]))),[])

# Accepted
# 77/77 cases passed (58 ms)
# Your runtime beats 5.07 % of python3 submissions
# Your memory usage beats 76.4 % of python3 submissions (14.1 MB)
