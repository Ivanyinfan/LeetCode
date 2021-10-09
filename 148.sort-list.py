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
        c,n,i=head,0,1
        while c: c,n=c.next,n+1
        h = ListNode(next=head)
        while i<n:
            t=h
            while True:
                f1,f2,s,m,k,c,e,l=0,0,t.next,t.next,0,t,None,False
                while k<i and m: m,k = m.next,k+1
                if not m: break
                while f1<i and f2<i and m:
                    if s.val<=m.val:
                        c.next = s
                        c,s,f1 = c.next,s.next,f1+1
                    else:
                        c.next = m
                        c,m,f2 = c.next, m.next,f2+1
                if f2==i or not m:
                    e = m
                    while f1<i:
                        c.next = s
                        c,s,f1 = c.next,s.next,f1+1
                    c.next = e
                    if not m: break
                elif f1==i:
                    while f2<i and m:
                        c.next = m
                        c,m,f2 = c.next, m.next,f2+1
                    if not m: break
                t=c
            i+=i
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
# 28/28 cases passed (548 ms)
# Your runtime beats 31.54 % of python3 submissions
# Your memory usage beats 37.09 % of python3 submissions (30.2 MB)
