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
        s, c = [root], root
        while c:
            if s and c==s[-1]:
                if c.left:
                    s.append(c.left)
                    c = c.left
                elif c.right:
                    s.append(c.right)
                    c = c.right
                else:
                    c = s.pop()
            else:
                r.append(c.val)
                if not s: return r
                if s[-1].left==c:
                    if s[-1].right:
                        s.append(s[-1].right)
                        c = s[-1]
                    else:
                        c = s.pop()
                else:
                    c = s.pop()
        return r


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
# Your memory usage beats 46.59 % of python3 submissions (14.3 MB)
