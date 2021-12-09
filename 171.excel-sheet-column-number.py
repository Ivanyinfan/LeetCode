#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    ord_A = ord('A')
    def titleToNumber(self, columnTitle: str) -> int:
        base = 1
        result = 0
        for i in range(len(columnTitle)-1, -1, -1):
            result += (ord(columnTitle[i])-Solution.ord_A+1)*base
            base*= 26
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.titleToNumber('A'), 1)
    test(sol.titleToNumber('AB'), 28)
    test(sol.titleToNumber('ZY'), 701)
    test(sol.titleToNumber('FXSHRXW'), 2147483647)

# Accepted
# 1002/1002 cases passed (32 ms)
# Your runtime beats 76.09 % of python3 submissions
# Your memory usage beats 44.14 % of python3 submissions (14.2 MB)
