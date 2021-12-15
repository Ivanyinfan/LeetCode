#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            newn = 0
            while n!=0:
                newn += (n%10)**2
                n = n//10
            if newn in visited:
                if newn == 1: return True
                return False
            visited.add(newn)
            n = newn
        return n==1
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isHappy(19), True)
    test(sol.isHappy(2), False)
    test(sol.isHappy(131), False)
    test(sol.isHappy(10), True)
    test(sol.isHappy(7), True) # 401

# Accepted
# 402/402 cases passed (28 ms)
# Your runtime beats 95.68 % of python3 submissions
# Your memory usage beats 16.3 % of python3 submissions (14.3 MB)
