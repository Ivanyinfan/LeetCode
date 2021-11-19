#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        dp=[[[None]*(l+1) for i in range(l+1)] for j in range(l+1)]
        for i in range(l+1):
            for j in range(l+1):
                dp[i][j][0]=True
        for i in range(1,l+1):
            for j in range(1, j+1):
                dp[i][j][1]=s1[i-1]==s2[j-1]
        for k in range(2, l+1):
            for i in range(1, l-k+1):
                for j in range(1, l-k+1):
                    if dp[i][j][k-1] and s1[i-1]==s2[j-1]: dp[i][j][k]=True
                    else:
                        l1=any([dp[i][j][t] and dp[i+t][j+t][k-t] for t in range(1,k)])
                        l2=any([dp[i][j-t][t] and dp[i+t][j][k-t] for t in range(1,k)])
                        dp[i][j][k] = l1 or l2
        return dp[1][1][-1]
# @lc code=end

