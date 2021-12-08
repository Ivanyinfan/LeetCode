#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
from typing import List
import bisect
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = bisect.bisect_left(numbers, target-numbers[start], 1, len(numbers)-1)
        while start!=end:
            add = numbers[start]+numbers[end]
            if add==target:
                return [start+1, end+1]
            if numbers[start]+numbers[end-1]>=target:
                end = end - 1
            else:
                start = start + 1
        return [start+1, end+1]

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.twoSum([2,7,11,15],9),[1,2])
    test(sol.twoSum([2,3,4],6),[1,3])
    test(sol.twoSum([-1,0],-1),[1,2])
    test(sol.twoSum([0,0],0),[1,2])
    test(sol.twoSum([5,25,75],100),[2,3]) #6

# Accepted
# 19/19 cases passed (71 ms)
# Your runtime beats 34.81 % of python3 submissions
# Your memory usage beats 5.47 % of python3 submissions (14.8 MB)
