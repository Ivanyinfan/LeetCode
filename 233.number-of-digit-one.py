#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        # for the k-th digit, the number of 1 is
        # (n/10^k) * 10^(k-1) + min( max(n%(10^k)- 10^(k-1) +1, 0), 10^(k-1)) )
        r = 0
        base = 1
        while base<=n:
            newbase = base*10
            maxx = max(n%newbase-base+1, 0)
            minn = min(maxx, base)
            r += (n//newbase)*base + minn
            base = newbase
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.countDigitOne(13),6)
    test(sol.countDigitOne(0),0)
    test(sol.countDigitOne(1),1)
    test(sol.countDigitOne(99),20)

# Accepted
# 38/38 cases passed (47 ms)
# Your runtime beats 11.29 % of python3 submissions
# Your memory usage beats 15.29 % of python3 submissions (14.3 MB)
