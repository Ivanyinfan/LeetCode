#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
from utils import ListNode, list2ListNode, listNode2List, test
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        f=s=ps=head
        while f and f.next:
            ps,s,f=s,s.next,f.next.next
        ps.next=None
        h1,h2 = self.sortList(head), self.sortList(s)
        h = ListNode()
        c = h
        while h1 and h2:
            if h1.val<h2.val:
                c.next = h1
                c, h1 = c.next, h1.next
            else:
                c.next = h2
                c, h2 = c.next, h2.next
        if h1: c.next = h1
        if h2: c.next = h2
        return h.next
       
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(listNode2List(sol.sortList(list2ListNode([]))),[])
    test(listNode2List(sol.sortList(list2ListNode([1]))),[1])
    test(listNode2List(sol.sortList(list2ListNode([2,1]))),[1,2])
    test(listNode2List(sol.sortList(list2ListNode([4,2,1,3]))),[1,2,3,4])   #E1
    test(listNode2List(sol.sortList(list2ListNode([-1,5,3,4,0]))),[-1,0,3,4,5]) #E2

# Accepted
# 28/28 cases passed (452 ms)
# Your runtime beats 72.43 % of python3 submissions
# Your memory usage beats 69.01 % of python3 submissions (30.1 MB)
