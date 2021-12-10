#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        if k==0: return
        for i in range(l//2):
            nums[i],nums[l-i-1] = nums[l-i-1], nums[i]
        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        for i in range((l-k)//2):
            nums[k+i], nums[l-i-1] = nums[l-i-1], nums[k+i]
        return nums
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.rotate([1,2,3,4,5,6,7], 6), [2,3,4,5,6,7,1])
    test(sol.rotate([1,2,3,4,5,6,7], 4), [4,5,6,7,1,2,3])
    test(sol.rotate([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])
    test(sol.rotate([-1,-100,3,99], 2), [3,99,-1,-100])
    test(sol.rotate([1,2,3,4,5,6,7,8], 4), [5,6,7,8,1,2,3,4])
    test(sol.rotate([1,2,3,4,5,6], 4), [3,4,5,6,1,2])

# Accepted
# 38/38 cases passed (216 ms)
# Your runtime beats 78.26 % of python3 submissions
# Your memory usage beats 56.97 % of python3 submissions (25.6 MB)
