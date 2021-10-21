#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
from utils import test
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e,m=0,len(nums)-1,0
        while s<=e:
            m = s+(e-s)//2
            if nums[m]>nums[e]:
                s = m + 1
            elif nums[m]<nums[e]:
                e = m
            else:
                if nums[s]>nums[e]:
                    e = m
                elif nums[s]<nums[e]:
                    e = m - 1
                else:
                    for i in range(s+1, m):
                        if nums[i]>nums[e]:
                            s = i + 1
                            break
                        if nums[i]<nums[e]:
                            s, e = s+1, i
                            break
                    else:
                        s = m + 1
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
    test(sol.findMin([1,3,5]), 1)
    test(sol.findMin([2,2,2,0,1]), 0)
    test(sol.findMin([2,2,2,2,2]), 2)
    test(sol.findMin([2]), 2)

# Accepted
# 192/192 cases passed (54 ms)
# Your runtime beats 57.6 % of python3 submissions
# Your memory usage beats 75.77 % of python3 submissions (14.8 MB)
