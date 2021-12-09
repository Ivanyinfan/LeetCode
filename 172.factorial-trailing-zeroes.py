#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        while n!=0:
            newn = n // 5
            r += newn
            n = newn
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.trailingZeroes(3),0)
    test(sol.trailingZeroes(5),1)
    test(sol.trailingZeroes(0),0)
    test(sol.trailingZeroes(25),6)

# Accepted
# 500/500 cases passed (28 ms)
# Your runtime beats 91.59 % of python3 submissions
# Your memory usage beats 45.01 % of python3 submissions (14.3 MB)
