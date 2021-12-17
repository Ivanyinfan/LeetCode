#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val==curr.val or q.val == curr.val:
                break
            flag1 = p.val>curr.val
            flag2 = q.val>curr.val
            if flag1!=flag2:
                break
            if flag1:
                curr = curr.right
            else: 
                curr = curr.left
        return curr
# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.lowestCommonAncestor(list2TreeNode([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(2),TreeNode(8)).val, 6)
    test(sol.lowestCommonAncestor(list2TreeNode([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(2),TreeNode(4)).val, 2)
    test(sol.lowestCommonAncestor(list2TreeNode([1,2]),TreeNode(2),TreeNode(1)).val, 1)
    test(sol.lowestCommonAncestor(list2TreeNode([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(0),TreeNode(4)).val, 2)
    test(sol.lowestCommonAncestor(list2TreeNode([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(7),TreeNode(9)).val, 8)
    test(sol.lowestCommonAncestor(list2TreeNode([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(4),TreeNode(7)).val, 6)

# Accepted
# 27/27 cases passed (85 ms)
# Your runtime beats 33.34 % of python3 submissions
# Your memory usage beats 46.05 % of python3 submissions (18.3 MB)
