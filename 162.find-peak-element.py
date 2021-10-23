#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
from utils import List, test
# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s,e=0,len(nums)-1
        while s<=e:
            m = s+(e-s)//2
            if m==len(nums)-1:return m
            if nums[m]<nums[m+1]:
                s = m + 1
            else:
                if m==0: return m
                if nums[m]>nums[m-1]: return m
                e = m - 1
        return s

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.findPeakElement([1]),0)
    test(sol.findPeakElement([1,2]),1)
    test(sol.findPeakElement([1,2,3,1]),2)
    test(sol.findPeakElement([1,2,1,3,5,6,4]),5)

# Accepted
# 63/63 cases passed (61 ms)
# Your runtime beats 31.72 % of python3 submissions
# Your memory usage beats 70.66 % of python3 submissions (14.3 MB)
