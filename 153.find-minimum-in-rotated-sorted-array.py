#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from utils import test
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e,m = 0,len(nums)-1,0
        while s<=e:
            m = (s+e)//2
            if nums[m]>=nums[e]:
                s = m + 1
            else:
                e = m
        return nums[m]
# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.findMin([3,4,5,1,2]),1)
    test(sol.findMin([4,5,6,7,0,1,2]),0)
    test(sol.findMin([11,13,15,17]),11)
    test(sol.findMin([1]),1)
    test(sol.findMin([1,2]),1)
    test(sol.findMin([2,1]),1)

# Accepted
# 150/150 cases passed (51 ms)
# Your runtime beats 42.55 % of python3 submissions
# Your memory usage beats 27.83 % of python3 submissions (14.7 MB)
