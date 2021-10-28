#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#
from typing import List
# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minn = min(nums)
        return sum([num-minn for num in nums])
        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minMoves([1,2,3]),3)
    test(sol.minMoves([1,1,1]),0)
        
# Accepted
# 84/84 cases passed (236 ms)
# Your runtime beats 94.7 % of python3 submissions
# Your memory usage beats 6.46 % of python3 submissions (15.8 MB)
