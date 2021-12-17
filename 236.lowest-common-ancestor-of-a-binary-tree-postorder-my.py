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

class Solution:
    def mergeAndReturn(self, curr, pre):
        curr[1] = pre[1] or curr[1]
        curr[2] = pre[2] or curr[2]
        if curr[1] and curr[2]:
            return curr[0]
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = list()
        curr = [root, root.val==p.val, root.val==q.val]
        pre = None
        while curr!=None or len(stack)!=0:
            # val_stack = list(map(lambda x:x[0].val, stack))
            while curr:
                stack.append(curr)
                if curr[0].left:
                    curr = [curr[0].left, curr[0].left.val==p.val, curr[0].left.val==q.val]
                else: break
            # val_stack = list(map(lambda x:x[0].val, stack))
            curr = stack[-1]
            if curr[0].right==None:
                curr = stack.pop()
                if pre and pre[0]==curr[0].left:
                    r = self.mergeAndReturn(curr, pre)
                    if r: return r
                pre = curr
                curr = None
            elif pre and curr[0].right==pre[0]:
                curr = stack.pop()
                r = self.mergeAndReturn(curr, pre)
                if r: return r
                pre = curr
                curr = None
            else:
                if pre and pre[0]==curr[0].left:
                    r = self.mergeAndReturn(curr, pre)
                    if r: return r
                if curr[0].right:
                    curr = [curr[0].right, curr[0].right.val==p.val, curr[0].right.val==q.val]
                else:
                    curr = None
        return None


        
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

# Time Limit Exceeded
# actually it is correct (passed all case)
# and the time complexity is n
