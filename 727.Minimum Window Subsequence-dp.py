#
# @lc app=leetcode id=727 lang=python3
#
# [727] Minimum Window Subsequence
#

# @lc code=start
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        l1, l2 = len(s1), len(s2)
        if l1<l2: return ''
        dp = [[None]*(l2+1) for i in range(l1+1)]
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(1, l2+1):
            dp[0][j] = -1
        for i in range(1,l1+1):
            for j in range(1,min(i+1,l2+1)):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if i-1>=j:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = -1
        minLen = float('inf')
        start = None
        for i in range(l2, l1+1):
            if dp[i][-1]!=-1:
                length = i - dp[i][-1]
                if length<minLen:
                    minLen = length
                    start = dp[i][-1]
        if start == None:
            return ''
        return s1[start:start+minLen]

        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minWindow("abcdebdde","bde"),"bcde")
    test(sol.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl",'u'),'')
    test(sol.minWindow("abcdebdde","aebdde"),"abcdebdde")
    test(sol.minWindow("a","a"),"a")
    test(sol.minWindow("ab","a"),"a")
    test(sol.minWindow("aa","a"),"a")
    test(sol.minWindow("bbbbdde","bde"),'bdde')

# Time Limit Exceeded
# 67 / 67 test cases passed, but took too long.
