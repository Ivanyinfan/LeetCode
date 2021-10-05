#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
from typing import Optional
from utils import ListNode, list2ListNode, listNode2List, node2List, test
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head1 = ListNode(0, head)
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if not slow.next: return head
        head2 = slow
        p1 = slow.next
        p2 = p1.next
        p1.next = None
        while p2:
            nextp2 = p2.next
            head2.next, p2.next = p2, p1
            p1,p2 = p2, nextp2
        head = c = ListNode(0)
        tail1 = head2
        head1, head2 = head1.next, head2.next
        tail1.next = None
        while head1 and head2:
            c.next = head1
            c, head1 = c.next, head1.next
            c.next = head2
            c, head2 = c.next, head2.next
        if head1:
            c.next, c = head1, c.next
        if head2:
            c.next, c = head2, c.next
        head = head.next
        return head

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(listNode2List(sol.reorderList(list2ListNode([1]))),[1])
    test(listNode2List(sol.reorderList(list2ListNode([1,2]))),[1,2])
    test(listNode2List(sol.reorderList(list2ListNode([1,2,3]))),[1,3,2])
    test(listNode2List(sol.reorderList(list2ListNode([1,2,3,4]))),[1,4,2,3])
    test(listNode2List(sol.reorderList(list2ListNode([1,2,3,4,5]))),[1,5,2,4,3]) # 2

# Accepted
# 12/12 cases passed (117 ms)
# Your runtime beats 26.59 % of python3 submissions
# Your memory usage beats 48.51 % of python3 submissions (23.4 MB)
