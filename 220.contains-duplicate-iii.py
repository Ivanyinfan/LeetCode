#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
from typing import List
# @lc code=start
class Solution:
    def getId(self, num, t):
        if num>=0:
            return num//(t+1)
        return -(-num//(t+1))-1
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k==0: return False
        bucket_map = dict()
        for i, num in enumerate(nums):
            if i>k:
                bucket_map.pop(self.getId(nums[i-k-1],t))
            index = self.getId(num,t)
            if index in bucket_map:
                return True
            left = num - t
            left_index = self.getId(left,t)
            if bucket_map.get(left_index, left-1)>=left:
                return True
            right = num + t
            right_index = self.getId(right,t)
            if bucket_map.get(right_index, right+1)<=right:
                return True
            bucket_map[index] = num
        return False
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0), True)
    test(sol.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2),True)
    test(sol.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3),False)

# Accepted
# 53/53 cases passed (140 ms)
# Your runtime beats 47.81 % of python3 submissions
# Your memory usage beats 61.9 % of python3 submissions (17.4 MB)

