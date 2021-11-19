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
                        first, second=c, pre
                    else:
                        second=c
                        break
                    c = None
                else:
                    pre=c
                    if c.right:
                        stack.append(c.right)
                        c = c.right.left
                    else:
                        break
            else:
                stack.append(c)
                c = c.left
        first.val, second.val = second.val, first.val
        return root

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(treeNode2List(sol.recoverTree(list2TreeNode([1,3,None,None,2]))),[3,1,None,None,2])
