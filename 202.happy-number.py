#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def getNext(self, n:int) -> int:
        r = 0
        while n!=0:
            r, n = r+(n%10)**2, n//10
        return r

    def isHappy(self, n: int) -> bool:
        fast = slow = n
        while True:
            fast = self.getNext(self.getNext(fast))
            slow = self.getNext(slow)
            if fast == 1:
                return True
            if fast == slow:
                break
        return False

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
# 402/402 cases passed (32 ms)
# Your runtime beats 85.19 % of python3 submissions
# Your memory usage beats 75.86 % of python3 submissions (14.1 MB)
