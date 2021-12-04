#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        dp = [i-1 for i in range(l+1)]
        for i in range(l):
            start = end = i
            while start>=0 and end<l and s[start]==s[end]:
                dp[end+1]=min(dp[end+1],dp[start]+1)
                start, end = start-1, end+1
            start, end = i, i+1
            while start>=0 and end<l and s[start]==s[end]:
                dp[end+1]=min(dp[end+1],dp[start]+1)
                start, end = start-1, end+1
        return dp[-1]

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minCut("aab"), 1)
    test(sol.minCut('ab'), 1)
    test(sol.minCut('a'), 0)
    test(sol.minCut('aaa'), 0)
    test(sol.minCut('abaaaaabba'),2)

# Accepted
# 33/33 cases passed (216 ms)
# Your runtime beats 96.18 % of python3 submissions
# Your memory usage beats 98.38 % of python3 submissions (14.2 MB)
