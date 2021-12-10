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
        start = 0
        count = 0
        while count<l:
            preIndex, preVal = start, nums[start]
            while True:
                newIndex = (preIndex+k)%l
                newVal = nums[newIndex]
                nums[newIndex] = preVal
                count += 1
                if newIndex == start:
                    break
                preIndex, preVal = newIndex, newVal
            start += 1
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
# 38/38 cases passed (232 ms)
# Your runtime beats 51.2 % of python3 submissions
# Your memory usage beats 13.76 % of python3 submissions (25.7 MB)

