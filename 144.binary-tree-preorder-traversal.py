#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
from utils import TreeNode, list2TreeNode, test
from typing import Optional,List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        c,r = root, list()
        while c:
            if not c.left:
                r.append(c.val)
                c = c.right
            else:
                t:TreeNode = c.left
                while t.right and t.right!=c:
                    t = t.right
                if (t.right):
                    t.right = None
                    c = c.right
                else:
                    t.right = c
                    r.append(c.val)
                    c = c.left
        return r
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.preorderTraversal(None),[])
    test(sol.preorderTraversal(list2TreeNode([1])),[1])
    test(sol.preorderTraversal(list2TreeNode([1,2,3])),[1,2,3])
    test(sol.preorderTraversal(list2TreeNode([1,2,3])),[1,2,3])
    test(sol.preorderTraversal(list2TreeNode([1,None,2,None,None,3])),[1,2,3])

# Accepted
# 69/69 cases passed (32 ms)
# Your runtime beats 67.26 % of python3 submissions
# Your memory usage beats 44.66 % of python3 submissions (14.3 MB)