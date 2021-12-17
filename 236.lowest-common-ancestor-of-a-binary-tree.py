#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
BOTH_PENDING = 2
LEFT_DONE = 1
BOTH_DONE = 0
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [[root, BOTH_PENDING]]
        find_one = False
        LCA = None
        while stack:
            # val_stack = list(map(lambda x:x[0].val, stack))
            node, status = stack[-1]
            if status==BOTH_DONE:
                stack.pop()
                # if node.val == p.val or node.val == q.val:
                if node == p or node == q:
                    if find_one:
                        if LCA>=len(stack):
                            return node
                        return stack[LCA][0]
                    find_one = True
                    LCA = len(stack)-1
                else:
                    if find_one and LCA>=len(stack):
                        LCA = len(stack)-1
            elif status == BOTH_PENDING:
                stack[-1][1] -= 1
                if node.left:
                    stack.append([node.left, BOTH_PENDING])
            else:
                stack[-1][1] -= 1
                if node.right:
                    stack.append([node.right, BOTH_PENDING])
        return root

# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.lowestCommonAncestor(list2TreeNode([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(5),TreeNode(1)).val,3)
    test(sol.lowestCommonAncestor(list2TreeNode([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(5),TreeNode(4)).val,5)
    test(sol.lowestCommonAncestor(list2TreeNode([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(7),TreeNode(4)).val,2)
    test(sol.lowestCommonAncestor(list2TreeNode([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(0),TreeNode(8)).val,1)
    test(sol.lowestCommonAncestor(list2TreeNode([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(2),TreeNode(0)).val,3)
    # test case 31
    last = None
    for i in range(9999, -1, -1):
        node = TreeNode(i, right=last)
        last = node
    root = last
    test(sol.lowestCommonAncestor(root,TreeNode(9999),TreeNode(9998)).val,9998)

# Accepted
# 31/31 cases passed (80 ms)
# Your runtime beats 36.36 % of python3 submissions
# Your memory usage beats 88.49 % of python3 submissions (18.3 MB)
