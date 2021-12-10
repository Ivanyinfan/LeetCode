#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        r = right
        while r!=0 and r>left: r = r&(r-1)
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.rangeBitwiseAnd(5,7),4)
    test(sol.rangeBitwiseAnd(0,0),0)
    test(sol.rangeBitwiseAnd(1,2147483647),0)
    test(sol.rangeBitwiseAnd(5,10),0)

# Accepted
# 8268/8268 cases passed (48 ms)
# Your runtime beats 95.01 % of python3 submissions
# Your memory usage beats 25.48 % of python3 submissions (14.3 MB)
