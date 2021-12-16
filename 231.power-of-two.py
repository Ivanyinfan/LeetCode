#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n&(n-1)==0 and n!=0
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isPowerOfTwo(1), True)
    test(sol.isPowerOfTwo(2), True)
    test(sol.isPowerOfTwo(3), False)
    test(sol.isPowerOfTwo(4), True)
    test(sol.isPowerOfTwo(5), False)
    test(sol.isPowerOfTwo(0), False) # 1108

# Accepted
# 1108/1108 cases passed (32 ms)
# Your runtime beats 69.95 % of python3 submissions
# Your memory usage beats 70.22 % of python3 submissions (14.2 MB)
