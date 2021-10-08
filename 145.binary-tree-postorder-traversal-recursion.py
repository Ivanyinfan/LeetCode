#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
from utils import TreeNode, list2TreeNode, test
from typing import Optional, List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = list()
        if not root: return r
        self.traverse(root, r)
        return r
    
    def traverse(self, root: TreeNode, r: list):
        if root.left:
            self.traverse(root.left, r)
        if root.right:
            self.traverse(root.right, r)
        r.append(root.val)
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.postorderTraversal(None),[])
    test(sol.postorderTraversal(list2TreeNode([1])),[1])
    test(sol.postorderTraversal(list2TreeNode([1,2,3])),[2,3,1])
    test(sol.postorderTraversal(list2TreeNode([1,None,2,None,None,3])),[3,2,1])

# Accepted
# 68/68 cases passed (32 ms)
# Your runtime beats 68.33 % of python3 submissions
# Your memory usage beats 12.87 % of python3 submissions (14.4 MB)
