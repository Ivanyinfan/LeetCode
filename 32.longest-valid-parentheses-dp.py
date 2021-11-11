#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[None]*(len(s)+1)
        dp[0]=0
        for i, char in enumerate(s):
            if char=='(':
                dp[i+1]=0
            else:
                j = i - dp[i] - 1
                if j<0:
                    dp[i+1]=0
                else:
                    if s[j]=='(':
                        dp[i+1]=dp[i]+2+dp[j]
                    else:
                        dp[i+1]=0
        return max(dp)
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.longestValidParentheses("(()"),2)
    test(sol.longestValidParentheses(")()())"),4)
    test(sol.longestValidParentheses(""),0)
    test(sol.longestValidParentheses("))))))"),0)
    test(sol.longestValidParentheses("((()()((()()))))"),16)

# Accepted
# 231/231 cases passed (44 ms)
# Your runtime beats 77.28 % of python3 submissions
# Your memory usage beats 76.95 % of python3 submissions (14.4 MB)
