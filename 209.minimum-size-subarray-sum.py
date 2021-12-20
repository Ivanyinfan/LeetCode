#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        start = 0
        end = 0
        r = l+1
        summ = 0
        while start<l and end<l+1:
            if summ<target:
                if end==l: break
                summ += nums[end]
                end += 1
            else:
                r = min(r, end-start)
                summ -= nums[start]
                start = start + 1
        return r if r<=l else 0
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 2)
    test(sol.minSubArrayLen(4, [1,4,4]), 1)
    test(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)
    test(sol.minSubArrayLen(1, [1]), 1)
    test(sol.minSubArrayLen(2, [1]), 0)

# Accepted
# 19/19 cases passed (76 ms)
# Your runtime beats 58.97 % of python3 submissions
# Your memory usage beats 41.63 % of python3 submissions (16.6 MB)
