#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
from typing import List
# @lc code=start
def maxProfit122(prices: List[int]) -> int:
    r = 0
    for i in range(1, len(prices)): r += max(prices[i]-prices[i-1],0)
    return r

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        l = len(prices)
        if not l or not k: return 0
        if 2*k>=l: return maxProfit122(prices)
        dp = [[[None]*2 for i in range(k+1)] for j in range(l)]
        dp = [[0,-prices[0]] for i in range(k+1)]
        for i in range(1, l):
            dp[-1] = [0, -prices[i]]
            for j in range(k-1, -1, -1):
                dp[j][0] = max(dp[j][0], dp[j][1]+prices[i])
                dp[j][1] = max(dp[j][1], dp[j+1][0]-prices[i])
        return max(map(lambda x:x[0], dp))


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.maxProfit(2, [2,4,1]), 2)
    test(sol.maxProfit(2, [3,2,6,5,0,3]), 7)
    test(sol.maxProfit(2, []), 0) # 3
    test(sol.maxProfit(2, [1]), 0)
    test(sol.maxProfit(2, [1, 2]), 1)
    test(sol.maxProfit(2, [2, 1]), 0)
    test(sol.maxProfit(0, [1, 2]), 0)
    test(sol.maxProfit(10, [3,2,6,5,0,3]), 7)
    test(sol.maxProfit(2, [3,3,5,0,0,3,1,4]),6) # 184

# Accepted
# 211/211 cases passed (132 ms)
# Your runtime beats 47.82 % of python3 submissions
# Your memory usage beats 33.76 % of python3 submissions (23 MB)
