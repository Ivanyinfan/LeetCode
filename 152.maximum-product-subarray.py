#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        z = [0]
        for i,n in enumerate(nums):
            if n==0: z.append(i)
        m = float('-inf')
        if len(z)>1:
            z.append(len(nums))
            for i in range(len(z)-1):
                m = max(m,z[i],z[i+1])
        
    def maxProduct2(self, s, e):
        for i in range(s, e):
            if self.nums[i]==0:
                if i==e-1:


        
# @lc code=end

