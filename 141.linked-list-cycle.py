#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#
from utils import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        head = ListNode(0, head)
        fast = slow = head
        while True:
            if fast==slow and fast!=head: return True
            if not fast or not fast.next: return False
            fast = fast.next.next
            slow = slow.next
        return False
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1
    print(sol.hasCycle(node1))
    node2.next = None
    print(sol.hasCycle(node1))

# Accepted
# 20/20 cases passed (52 ms)
# Your runtime beats 84.18 % of python3 submissions
# Your memory usage beats 24.53 % of python3 submissions (17.8 MB)
