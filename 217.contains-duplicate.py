#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import List
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.containsDuplicate([1,2,3,1]), True)
    test(sol.containsDuplicate([1,2,3,4]), False)
    test(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)
    test(sol.containsDuplicate([1]), False)
    test(sol.containsDuplicate([1, 1]), True)

# Accepted
# 20/20 cases passed (120 ms)
# Your runtime beats 66.04 % of python3 submissions
# Your memory usage beats 63.84 % of python3 submissions (20 MB)
