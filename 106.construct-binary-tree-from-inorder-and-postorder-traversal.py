#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
from typing import List, Optional
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder = inorder
        self.postorder = postorder
        self.posMap = dict()
        for i, num in enumerate(inorder):
            self.posMap[num]=i
        return self.buildTree2(0, len(inorder), 0, len(postorder))

    def buildTree2(self, s1, e1, s2, e2) -> Optional[TreeNode]:
        if s1>=e1 or s2>=e2: return None
        root = self.postorder[e2-1]
        pos = self.posMap[root]
        left_nums = pos - s1
        left = self.buildTree2(s1, pos, s2, s2+left_nums)
        right = self.buildTree2(pos+1, e1, s2+left_nums, e2-1)
        return TreeNode(root, left, right)

# @lc code=end
from utils import test, treeNode2List
if __name__ == "__main__":
    sol = Solution()
    test(treeNode2List(sol.buildTree([9,3,15,20,7], [9,15,7,20,3])),[3,9,20,None,None,15,7])
    test(treeNode2List(sol.buildTree([-1], [-1])),[-1])
    test(treeNode2List(sol.buildTree([2,1,3], [2,3,1])),[1,2,3])
    test(treeNode2List(sol.buildTree([2,1], [2,1])),[1,2])
    test(treeNode2List(sol.buildTree([1,3], [3,1])),[1,None,3])

# Accepted
# 202/202 cases passed (60 ms)
# Your runtime beats 74.15 % of python3 submissions
# Your memory usage beats 76.71 % of python3 submissions (19 MB)
