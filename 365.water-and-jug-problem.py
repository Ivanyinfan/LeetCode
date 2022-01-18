#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#
from typing import List
# @lc code=start
from collections import deque
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def addItem(item):
            nonlocal stack, histroy
            if item not in histroy:
                histroy.add(item)
                stack.append(item)
        if targetCapacity>jug1Capacity+jug2Capacity:
            return False
        stack = deque([(jug1Capacity,0),(0,jug2Capacity), (jug1Capacity,jug2Capacity)])
        histroy = {(jug1Capacity,0), (0,jug2Capacity), (jug1Capacity,jug2Capacity)}
        while stack:
            status = stack.popleft()
            summ = sum(status)
            if summ==targetCapacity:
                return True
            if status[0]!=0:
                addItem((0, status[1]))
            if status[1]!=0:
                addItem((status[0], 0))
            if status[0]!=jug1Capacity:
                addItem((jug1Capacity, status[1]))
            if status[1]!=jug2Capacity:
                addItem((status[0], jug2Capacity))
            if status[0]!=0 and status[1]!=jug2Capacity:
                new2 = min(jug2Capacity, summ)
                addItem((status[0]-(new2-jug2Capacity), new2))
            if status[1]!=0 and status[0]!=jug1Capacity:
                new1 = min(jug1Capacity, summ)
                addItem((new1, status[1]-(new1-status[0])))
        return False
        
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    print(sol.canMeasureWater(3,5,4))
    print(sol.canMeasureWater(2,6,5))
    print(sol.canMeasureWater(1,2,5))

# 28 / 28 test cases passed.
# Status: Accepted
# Runtime: 2640 ms
# Memory Usage: 88 MB
# Your runtime beats 25.68 % of python3 submissions.
# Your memory usage beats 13.33 % of python3 submissions.
