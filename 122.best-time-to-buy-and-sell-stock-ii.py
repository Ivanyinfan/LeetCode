#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 0
        for i in range(1, len(prices)): r += max(prices[i]-prices[i-1],0)
        return r
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.maxProfit([7,1,5,3,6,4]), 7)
    test(sol.maxProfit([1,2,3,4,5]), 4)
    test(sol.maxProfit([7,6,4,3,1]), 0)
    test(sol.maxProfit([0]), 0)

# Accepted
# 200/200 cases passed (52 ms)
# Your runtime beats 97.69 % of python3 submissions
# Your memory usage beats 24.12 % of python3 submissions (15.1 MB)
