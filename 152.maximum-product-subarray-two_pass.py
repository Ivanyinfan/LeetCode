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
        neg, s, m = list(), 0, float('-inf')
        for i, num in enumerate(nums):
            if num==0:
                m = max(self.maxProduct2(nums,neg,s,i), max(m,0))
                s = i + 1
                neg = list()
            elif num<0: neg.append(i)
        m = max(m, self.maxProduct2(nums, neg, s, len(nums)))
        return m

    def maxProduct2(self, nums, neg, s, e):
        if s>=e: return float('-inf')
        if e-s==1: return nums[s]
        product = [None]*(e-s)
        product[0]=nums[s]
        for i in range(s+1,e): product[i-s]=product[i-1-s]*nums[i]
        if len(neg)%2==0: return product[-1]
        f,l = neg[0], neg[-1]
        m = product[-1]//product[f-s]
        if l>s: m = max(product[l-1-s], m)
        return m

        
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
# 187/187 cases passed (88 ms)
# Your runtime beats 19.53 % of python3 submissions
# Your memory usage beats 10.33 % of python3 submissions (15.5 MB)
