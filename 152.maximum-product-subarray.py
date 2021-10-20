#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from utils import test
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx,minn,re,t = nums[0],nums[0],nums[0],[None]*3
        for i in range(1, len(nums)):
            t[0], t[1], t[2] = nums[i], nums[i]*maxx, nums[i]*minn
            maxx, minn = max(t), min(t)
            re = max(re, maxx)
        return re
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.maxProduct([2,3,-2,4]),6)
    test(sol.maxProduct([-2,0,-1]),0)
    test(sol.maxProduct([0]),0)
    test(sol.maxProduct([-1]),-1)
    test(sol.maxProduct([-1, -1]),1)
    test(sol.maxProduct([-1, -1, -1]),1)
    test(sol.maxProduct([-3,0,1,-2]), 1)    #18
    test(sol.maxProduct([1,0,0,0]),1)   #176

# Accepted
# 187/187 cases passed (90 ms)
# Your runtime beats 17.86 % of python3 submissions
# Your memory usage beats 95.28 % of python3 submissions (14.1 MB)
