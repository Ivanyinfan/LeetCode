#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        r = 0
        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    r+=node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return r
# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.sumOfLeftLeaves(list2TreeNode([3,9,20,None,None,15,7])),24)
    test(sol.sumOfLeftLeaves(list2TreeNode([3])),0)
    test(sol.sumOfLeftLeaves(list2TreeNode([3,9,20,4,None,15,7])),19)
    test(sol.sumOfLeftLeaves(list2TreeNode([3,9,20,4,5,15,7])),19)
    test(sol.sumOfLeftLeaves(list2TreeNode([1,2,3])),2)
    test(sol.sumOfLeftLeaves(list2TreeNode([1,2])),2)
    test(sol.sumOfLeftLeaves(list2TreeNode([1,None,3])),0)

# Accepted
# 100/100 cases passed (32 ms)
# Your runtime beats 69.39 % of python3 submissions
# Your memory usage beats 76.02 % of python3 submissions (14.6 MB)
