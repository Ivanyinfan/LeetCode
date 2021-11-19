#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        dp=[[[None]*(l+1) for i in range(l)] for j in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i][j][1]=s1[i]==s2[j]
        for k in range(2, l+1):
            for i in range(l-k+1):
                for j in range(l-k+1):
                    l1=any([dp[i][j][t] and dp[i+t][j+t][k-t] for t in range(1,k)])
                    l2=any([dp[i][j+k-t][t] and dp[i+t][j][k-t] for t in range(1,k)])
                    dp[i][j][k] = l1 or l2
        return dp[0][0][l]
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isScramble('great','rgeat'),True)
    test(sol.isScramble('abcde','caebd'),False)
    test(sol.isScramble('a','a'),True)
    test(sol.isScramble('great','rgtea'),True)
    test(sol.isScramble('great','rgtae'),True)
    test(sol.isScramble('great','rgaet'),True)
    test(sol.isScramble('great','eatrg'),True)
    test(sol.isScramble('great','tearg'),True)
    test(sol.isScramble('great','aetgr'),True)
    test(sol.isScramble("abcdbdacbdac","bdacabcdbdac"), True) #281
    test(sol.isScramble("abcdbdacbdac","bdacabcdacbd"), True)
    test(sol.isScramble("abcd","bdac"), False)
    test(sol.isScramble("great","tearg"), True)

# Accepted
# 288/288 cases passed (612 ms)
# Your runtime beats 7.03 % of python3 submissions
# Your memory usage beats 67.58 % of python3 submissions (14.7 MB)
