#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = list()
        while curr!=None or len(stack)!=0:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if k==1:
                return curr.val
            k -= 1
            curr = curr.right
        return 0
# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.kthSmallest(list2TreeNode([3,1,4,None,2]),1), 1)
    test(sol.kthSmallest(list2TreeNode([5,3,6,2,4,None,None,1]),3), 3)
    test(sol.kthSmallest(list2TreeNode([5]),1), 5)

# Accepted
# 93/93 cases passed (73 ms)
# Your runtime beats 13.91 % of python3 submissions
# Your memory usage beats 84.95 % of python3 submissions (17.9 MB)
