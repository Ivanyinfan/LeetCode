#
# @lc app=leetcode id=708 lang=python3
#
# [708] Insert into a Sorted Circular Linked List
#
from typing import List, Optional
from utils import CircularListNode2List, Node
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        current = head
        node = Node(insertVal)
        first_equal = None
        while True:
            if current.val < current.next.val:
                if insertVal>=current.val and insertVal<=current.next.val:
                    break
            elif current.val > current.next.val:
                if insertVal>=current.val or insertVal<=current.next.val:
                    break
            else:
                if first_equal == None:
                    first_equal = current
                elif first_equal == current:
                    break
            current = current.next
        current.next, node.next = node, current.next
        return head

# @lc code=end
from utils import test, List2CircularListNode
if __name__ == "__main__":
    sol = Solution()
    test(CircularListNode2List(sol.insert(List2CircularListNode([3,4,1]), 2)),[3,4,1,2])
    test(CircularListNode2List(sol.insert(List2CircularListNode([]), 1)),[1])
    test(CircularListNode2List(sol.insert(List2CircularListNode([1]), 0)),[1,0])
    test(CircularListNode2List(sol.insert(List2CircularListNode([1,2]), 0)),[1,2,0])
    test(CircularListNode2List(sol.insert(List2CircularListNode([3,4,4]), 4)),[3,4,4,4])
    test(CircularListNode2List(sol.insert(List2CircularListNode([3,4,1]), 1)),[3,4,1,1])

# 执行结果：通过
# 显示详情
# 添加备注

# 执行用时：44 ms, 在所有 Python3 提交中击败了25.17%的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了30.77%的用户
# 通过测试用例：108 / 108
