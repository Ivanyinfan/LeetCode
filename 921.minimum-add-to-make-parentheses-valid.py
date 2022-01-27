#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        leftCount = 0
        result = 0
        for char in s:
            if char == '(':
                leftCount += 1
            else:
                if leftCount == 0:
                    result += 1
                else:
                    leftCount -= 1
        return result+leftCount
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minAddToMakeValid("())"),1)
    test(sol.minAddToMakeValid("((("),3)
    test(sol.minAddToMakeValid(""),0)
    test(sol.minAddToMakeValid("("),1)
    test(sol.minAddToMakeValid(")"),1)
    test(sol.minAddToMakeValid("()"),0)

# Accepted
# 115/115 cases passed (49 ms)
# Your runtime beats 24.12 % of python3 submissions
# Your memory usage beats 69.78 % of python3 submissions (14.1 MB)
