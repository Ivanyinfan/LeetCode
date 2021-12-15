#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def getHeight(self, root:TreeNode):
        height = 0
        while root:
            height, root = height+1, root.left
        return height

    def countNodes(self, root: Optional[TreeNode]) -> int:
        nodes_num = 0
        while root:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            if left_height == right_height:
                nodes_num += (1<<left_height)
                root = root.right
            else:
                nodes_num += (1<<right_height)
                root = root.left
        return nodes_num 
              
# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.countNodes(None), 0)
    test(sol.countNodes(list2TreeNode([1,2,3,4,5,6])),6)
    test(sol.countNodes(list2TreeNode([1])),1)
    test(sol.countNodes(list2TreeNode([1,2,3,4,5,6,7])),7)
    for i in range(2, 16):
        root = list2TreeNode([j for j in range(1, i)])
        test(sol.countNodes(root), i-1)

# Accepted
# 18/18 cases passed (152 ms)
# Your runtime beats 6.18 % of python3 submissions
# Your memory usage beats 16.61 % of python3 submissions (21.6 MB)
