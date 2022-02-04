#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
from typing import List
# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0]>k:
            return k
        missed = arr[0] - 1
        for i in range(1, len(arr)):
            missed+=arr[i]-arr[i-1]-1
            if missed>=k:
                return arr[i]-(missed-k+1)
        return arr[-1]+k-missed

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findKthPositive([2,3,4,7,11],5),9)
    test(sol.findKthPositive([1,2,3,4],2),6)
    test(sol.findKthPositive([2,3,4],1),1)
    test(sol.findKthPositive([2,3,4],2),5)

# Accepted
# 84/84 cases passed (96 ms)
# Your runtime beats 20.35 % of python3 submissions
# Your memory usage beats 99.01 % of python3 submissions (14 MB)
