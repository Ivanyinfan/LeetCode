#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return max(self.getLen(s, '('), self.getLen(reversed(s),')'))     

    def getLen(self, s, leftSign):
        left, right, r = 0, 0, 0
        for char in s:
            if char==leftSign: left+=1
            else: right+=1
            if right==left: r = max(r, right+left)
            elif right>left: left,right=0,0
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.longestValidParentheses("(()"),2)
    test(sol.longestValidParentheses(")()())"),4)
    test(sol.longestValidParentheses(""),0)
    test(sol.longestValidParentheses("))))))"),0)
    test(sol.longestValidParentheses("((()()((()()))))"),16)
    test(sol.longestValidParentheses("((()((()()"),4)

# Accepted
# 231/231 cases passed (40 ms)
# Your runtime beats 91.39 % of python3 submissions
# Your memory usage beats 88.67 % of python3 submissions (14.4 MB)
