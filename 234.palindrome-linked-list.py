#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
from typing import Optional
from utils import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        current = head
        while current: n, current = n+1, current.next
        reverse_num = n//2
        pre, cur, next = None, head, head.next
        while reverse_num:
            cur.next = pre
            pre, cur, next = cur, next, next.next
            reverse_num -= 1
        head1 = pre
        head2 = cur if n%2==0 else next
        while head1 and head2:
            if head1.val!=head2.val:
                return False
            head1, head2 = head1.next, head2.next
        return True


# @lc code=end
from utils import test, list2ListNode
if __name__ == "__main__":
    sol = Solution()
    test(sol.isPalindrome(list2ListNode([1,2,2,1])), True)
    test(sol.isPalindrome(list2ListNode([1,2])), False)
    test(sol.isPalindrome(list2ListNode([1,2])), False)
    test(sol.isPalindrome(list2ListNode([1])), True)
    test(sol.isPalindrome(list2ListNode([1,1])), True)
    test(sol.isPalindrome(list2ListNode([1,1,1])), True)
    test(sol.isPalindrome(list2ListNode([1,2,3,2,1])), True)
    test(sol.isPalindrome(list2ListNode([1,2,3,1,1])), False)
    test(sol.isPalindrome(list2ListNode([1,2,3,2,2])), False)

# Accepted
# 85/85 cases passed (815 ms)
# Your runtime beats 62.19 % of python3 submissions
# Your memory usage beats 96.3 % of python3 submissions (31.5 MB)
