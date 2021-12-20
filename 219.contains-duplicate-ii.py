#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if i>k:
                index = i-k-1
                seen.remove(nums[index])
            if num in seen:
                return True
            seen.add(num)
        return False

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.containsNearbyDuplicate([1,2,3,1],3),True)
    test(sol.containsNearbyDuplicate([1,0,1,1],1),True)
    test(sol.containsNearbyDuplicate([1,2,3,1,2,3],2),False)

# Accepted
# 51/51 cases passed (616 ms)
# Your runtime beats 57.45 % of python3 submissions
# Your memory usage beats 92.79 % of python3 submissions (25.7 MB)
