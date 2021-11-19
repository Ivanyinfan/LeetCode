#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
from typing import Optional
from utils import TreeNode, list2TreeNode, treeNode2List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack,pre=[root],None
        c = root.left
        first = second = None
        while stack:
            if not c:
                c = stack.pop()
                if pre!=None and c.val<pre.val:
                    if first==None:
                        first, second=pre, c
                    else:
                        second=c
                        break
                pre=c
                if c.right:
                    stack.append(c.right)
                    c = c.right.left
                else:
                    c = None
            else:
                stack.append(c)
                c = c.left
        first.val, second.val = second.val, first.val
        return root

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    # test(treeNode2List(sol.recoverTree(list2TreeNode([1,3,None,None,2]))),[3,1,None,None,2])
    test(treeNode2List(sol.recoverTree(list2TreeNode([3,1,4,None,None,2,None]))),[2,1,4,None,None,3])

# Accepted
# 1919/1919 cases passed (72 ms)
# Your runtime beats 79.13 % of python3 submissions
# Your memory usage beats 56.1 % of python3 submissions (14.6 MB)
