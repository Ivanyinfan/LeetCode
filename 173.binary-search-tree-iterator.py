#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
from typing import Optional
from utils import TreeNode
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = list()

    def next(self) -> int:
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        r = self.cur.val
        self.cur = self.cur.right
        return r

    def hasNext(self) -> bool:
        return self.cur!=None or len(self.stack)!=0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
from utils import test, list2TreeNode
if __name__ == "__main__":
    iterator = BSTIterator(list2TreeNode([7, 3, 15, None, None, 9, 20]))
    test(iterator.hasNext(),True)
    test(iterator.next(),3)
    test(iterator.hasNext(),True)
    test(iterator.next(),7)
    test(iterator.hasNext(),True)
    test(iterator.next(),9)
    test(iterator.hasNext(),True)
    test(iterator.next(),15)
    test(iterator.hasNext(),True)
    test(iterator.next(),20)
    test(iterator.hasNext(),False)

# Accepted
# 61/61 cases passed (128 ms)
# Your runtime beats 7.29 % of python3 submissions
# Your memory usage beats 30.85 % of python3 submissions (20.7 MB)
