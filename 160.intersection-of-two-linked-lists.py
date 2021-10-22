#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
from utils import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        c1,c2=headA,headB
        while c1!=c2:
            c1=c1.next if c1 else headB
            c2=c2.next if c2 else headA
        return c1
# @lc code=end

# Accepted
# 39/39 cases passed (231 ms)
# Your runtime beats 20.81 % of python3 submissions
# Your memory usage beats 94.88 % of python3 submissions (29.3 MB)
