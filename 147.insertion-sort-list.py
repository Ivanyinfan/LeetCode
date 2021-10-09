#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
from utils import ListNode, list2ListNode, listNode2List, node2List, test
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        c:ListNode = head.next
        head.next = None
        while c:
            newc = c.next
            if c.val < head.val:
                c.next = head
                head = c
            else:
                c2=head
                while c2.next and c2.next.val<=c.val:
                    c2 = c2.next
                c.next = c2.next
                c2.next = c
            c = newc
        return head
                
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(listNode2List(sol.insertionSortList(list2ListNode([]))),[])
    test(listNode2List(sol.insertionSortList(list2ListNode([1]))),[1])
    test(listNode2List(sol.insertionSortList(list2ListNode([2,1]))),[1,2])
    test(listNode2List(sol.insertionSortList(list2ListNode([4,2,1,3]))),[1,2,3,4])  #E1
    test(listNode2List(sol.insertionSortList(list2ListNode([-1,5,3,4,0]))),[-1,0,3,4,5])  #E2

# Accepted
# 19/19 cases passed (2016 ms)
# Your runtime beats 21.05 % of python3 submissions
# Your memory usage beats 98.69 % of python3 submissions (16.2 MB)
