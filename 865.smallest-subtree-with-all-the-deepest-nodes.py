#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, level, info):
        l_level = r_level = level
        if node.left: 
            l_level = self.dfs(node.left, level+1, info)
        if node.right:
            r_level = self.dfs(node.right, level+1, info)
        max_level = info[0]
        level = max(l_level, r_level)
        if l_level>=max_level and r_level>=max_level:
            info[0] = level
            info[1] = node
        return level

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None
        info = [0, root]
        self.dfs(root, 0, info)
        return info[1]

# @lc code=end
from utils import test, list2TreeNode, treeNode2List
if __name__ == "__main__":
    sol = Solution()
    root = list2TreeNode([3,5,1,6,2,0,8,None,None,7,4])
    ans = treeNode2List(sol.subtreeWithAllDeepest(root))
    test(ans, [2,7,4])

    root = list2TreeNode([1])
    ans = treeNode2List(sol.subtreeWithAllDeepest(root))
    test(ans, [1])

    root = list2TreeNode([0,1,3,None,2])
    ans = treeNode2List(sol.subtreeWithAllDeepest(root))
    test(ans, [2])

# Success
# Details
# Runtime: 49 ms, faster than 49.49% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
# Memory Usage: 14.1 MB, less than 81.57% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
