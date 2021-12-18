#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import List
from collections import deque
# @lc code=start
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        r = list()
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]]<=num: queue.pop()
            queue.append(i)
            if i>=k-1:
                if queue[0]<=i-k: queue.popleft()
                r.append(nums[queue[0]])
        return r


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3),[3,3,5,5,6,7])
    test(sol.maxSlidingWindow(nums = [1], k = 1),[1])
    test(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 4),[3,5,5,6,7])
    test(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 8),[7])
    test(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 1),[1,3,-1,-3,5,3,6,7])

# Accepted
# 61/61 cases passed (2273 ms)
# Your runtime beats 23.88 % of python3 submissions
# Your memory usage beats 82.71 % of python3 submissions (29.6 MB)

