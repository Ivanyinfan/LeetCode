#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
from typing import List
# @lc code=start
class Solution:
    def getRange(self, nums, start, end):
        if start == end:
            return str(nums[start])
        return f'{nums[start]}->{nums[end]}'

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return list()
        start = 0
        r = list()
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                r.append(self.getRange(nums, start, i-1))
                start = i
        r.append(self.getRange(nums, start, len(nums)-1))
        return r

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.summaryRanges([0,1,2,4,5,7]), ["0->2","4->5","7"])
    test(sol.summaryRanges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])

# Accepted
# 28/28 cases passed (40 ms)
# Your runtime beats 14.73 % of python3 submissions
# Your memory usage beats 14.96 % of python3 submissions (14.3 MB)
