#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        l = len(nums)
        for i in range(1, l):
            result[i] = result[i-1]*nums[i-1]
        suffix = 1
        for i in range(l-1, -1, -1):
            result[i] *= suffix
            suffix*=nums[i]
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.productExceptSelf([1,2,3,4]),[24,12,8,6])
    test(sol.productExceptSelf([-1,1,0,-3,3]),[0,0,9,0,0])
    test(sol.productExceptSelf([1,2]),[2,1])

# Accepted
# 20/20 cases passed (365 ms)
# Your runtime beats 11.43 % of python3 submissions
# Your memory usage beats 59.01 % of python3 submissions (21.1 MB)
