#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = list()
        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap, num)
            elif num>heap[0]:
                heapq.heappushpop(heap, num)
        return heap[0]
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findKthLargest([3,2,1,5,6,4], 2), 5)
    test(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4), 4)
    test(sol.findKthLargest([1,2], 2), 1)
    test(sol.findKthLargest([1], 1), 1)

# Accepted
# 32/32 cases passed (48 ms)
# Your runtime beats 99.9 % of python3 submissions
# Your memory usage beats 48.47 % of python3 submissions (15.2 MB)
