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
        s,c=set(),headA
        while c:
            s.add(c)
            c=c.next
        c=headB
        while c:
            if c in s: return c
            c = c.next
        return None
# @lc code=end

# Accepted
# 39/39 cases passed (207 ms)
# Your runtime beats 28.37 % of python3 submissions
# Your memory usage beats 23.15 % of python3 submissions (29.8 MB)
