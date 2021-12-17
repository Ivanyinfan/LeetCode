#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#
from utils import ListNode, test
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # return node

# @lc code=end
from utils import test, list2ListNode, listNode2List, getListNodeByVal
if __name__ == "__main__":
    sol = Solution()
    a = list2ListNode([4,5,1,9])
    node = getListNodeByVal(a, 5)
    sol.deleteNode(node)
    test(listNode2List(a),[4,1,9])
    a = list2ListNode([4,5,1,9])
    node = getListNodeByVal(a, 1)
    sol.deleteNode(node)
    test(listNode2List(a),[4,5,9])
    a = list2ListNode([4,5,1,9])
    node = getListNodeByVal(a, 4)
    sol.deleteNode(node)
    test(listNode2List(a),[5,1,9])

# Accepted
# 41/41 cases passed (55 ms)
# Your runtime beats 13.18 % of python3 submissions
# Your memory usage beats 62.01 % of python3 submissions (14.7 MB)
