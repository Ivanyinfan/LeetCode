#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
from utils import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        head = ListNode(0, head)
        fast = slow = head
        while True:
            if fast==slow and fast!=head: break
            if not fast or not fast.next: return None
            fast = fast.next.next
            slow = slow.next
        pt1 = head
        pt2 = fast
        while pt1!=pt2:
            pt1 = pt1.next
            pt2 = pt2.next
        return pt1
# @lc code=end

# Accepted
# 16/16 cases passed (52 ms)
# Your runtime beats 66.43 % of python3 submissions
# Your memory usage beats 54.16 % of python3 submissions (17.2 MB)
