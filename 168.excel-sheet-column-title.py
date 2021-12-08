#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    ord_A = ord('A')
    def convertToTitle(self, columnNumber: int) -> str:
        r = list()
        while columnNumber:
            remainer = columnNumber%26
            if remainer==0:
                r.append('Z')
                columnNumber = columnNumber//26-1
            else:
                r.append(chr(remainer+Solution.ord_A-1))
                columnNumber //= 26
        return ''.join(reversed(r))
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.convertToTitle(1),'A')
    test(sol.convertToTitle(28),'AB')
    test(sol.convertToTitle(701),'ZY')
    test(sol.convertToTitle(2147483647),"FXSHRXW")
    test(sol.convertToTitle(26),"Z")
    test(sol.convertToTitle(52),"AZ")

# Accepted
# 18/18 cases passed (40 ms)
# Your runtime beats 18.5 % of python3 submissions
# Your memory usage beats 72.63 % of python3 submissions (14.1 MB)
