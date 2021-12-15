#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
from typing import Optional, List
from utils import ListNode, list2ListNode, listNode2List
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = sentinel= ListNode(next=head)
        cur = head
        while cur!=None:
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre, cur = pre.next, cur.next
        return sentinel.next
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(listNode2List(sol.removeElements(list2ListNode([1,2,6,3,4,5,6]), 6)), [1,2,3,4,5])
    test(listNode2List(sol.removeElements(list2ListNode([]), 1)), [])
    test(listNode2List(sol.removeElements(list2ListNode([7,7,7,7]), 7)), [])

# Accepted
# 66/66 cases passed (64 ms)
# Your runtime beats 88.61 % of python3 submissions
# Your memory usage beats 89.93 % of python3 submissions (17.1 MB)
