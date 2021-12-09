#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
from typing import List
# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [float('inf')]*(n+1)
        dp[-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                bit = dungeon[i][j]
                dp[j]=min(dp[j],dp[j+1])-bit
                if bit<0:
                    dp[j] = max(1-bit, dp[j])
                dp[-1]=float('inf')
        return max(dp[0], 1)
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]), 7)
    test(sol.calculateMinimumHP([[0]]), 1)
    test(sol.calculateMinimumHP([[100]]), 1) # 39
    test(sol.calculateMinimumHP([[-100]]), 101)

# Accepted
# 45/45 cases passed (72 ms)
# Your runtime beats 78.51 % of python3 submissions
# Your memory usage beats 98.18 % of python3 submissions (15 MB)
