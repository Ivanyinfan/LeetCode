#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
from typing import List, Optional
from utils import TreeNode, treeNode2List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.posMap = dict()
        self.preorder = preorder
        self.inorder = inorder
        for i, num in enumerate(inorder):
            self.posMap[num]=i
        return self.buildTree2(0, len(preorder), 0, len(inorder))

    def buildTree2(self, s1, e1, s2, e2):
        if s1>=e1 or s2>=e2: return None
        pos = self.posMap[self.preorder[s1]]
        left_nums = pos - s2
        left = self.buildTree2(s1+1, s1+1+left_nums, s2, pos)
        right = self.buildTree2(s1+1+left_nums, e1, pos+1, e2)
        return TreeNode(self.preorder[s1], left, right)

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(treeNode2List(sol.buildTree([3,9,20,15,7], [9,3,15,20,7])),[3,9,20,None,None,15,7])
    test(treeNode2List(sol.buildTree([-1], [-1])),[-1])
    test(treeNode2List(sol.buildTree([1,2,3], [2,1,3])),[1,2,3])
    test(treeNode2List(sol.buildTree([1,2], [2,1])),[1,2])
    test(treeNode2List(sol.buildTree([1,3], [1,3])),[1,None,3])

# Accepted
# 203/203 cases passed (60 ms)
# Your runtime beats 81.18 % of python3 submissions
# Your memory usage beats 98.18 % of python3 submissions (18 MB)
