#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
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

    def DFS(self, node, result):
        if not node.left:
            left_height = 0
        else:
            left_height = self.DFS(node.left, result)
        if not node.right:
            right_height = 0
        else:
            right_height = self.DFS(node.right, result)
        height =  max(left_height, right_height)+1
        if len(result)<height:
            result.append(list())
        result[height-1].append(node.val)
        return height

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = list()
        self.DFS(root, result)
        return result


# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.findLeaves(root = list2TreeNode([1,2,3,4,5])), [[4,5,3],[2],[1]])
    test(sol.findLeaves(root = list2TreeNode([1])), [[1]])
    test(sol.findLeaves(root = list2TreeNode([1,2])), [[2], [1]])
    test(sol.findLeaves(root = list2TreeNode([1,2,3])), [[2,3],[1]])

# Success
# Details 
# Runtime: 32 ms, faster than 72.71% of Python3 online submissions for Find Leaves of Binary Tree.
# Memory Usage: 14.3 MB, less than 59.40% of Python3 online submissions for Find Leaves of Binary Tree.
