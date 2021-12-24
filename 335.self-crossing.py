#
# @lc app=leetcode id=335 lang=python3
#
# [335] Self Crossing
#
from typing import List
# @lc code=start
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(len(distance)):
            if i>=3 and distance[i-1]<=distance[i-3] and distance[i]>=distance[i-2]:
                return True
            if i>=4 and distance[i-1]==distance[i-3] and distance[i]+distance[i-4]>=distance[i-2]:
                return True
            if i>=5 and distance[i-1]<=distance[i-3] and distance[i-1]+distance[i-5]>=distance[i-3] and distance[i-2]>distance[i-4] and distance[i]+distance[i-4]>=distance[i-2]:
                return True
        return False
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isSelfCrossing([2,1,1,2]),True)
    test(sol.isSelfCrossing([1,2,3,4]),False)
    test(sol.isSelfCrossing([1,1,1,1]),True)
    
# Accepted
# 29/29 cases passed (160 ms)
# Your runtime beats 76.24 % of python3 submissions
# Your memory usage beats 89.11 % of python3 submissions (22.2 MB)
