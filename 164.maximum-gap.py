#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
import math
from random import shuffle
from utils import test
from typing import List
# @lc code=start
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxx,minn=max(nums),min(nums)
        if maxx==minn: return 0
        k = math.ceil((maxx-minn)/(len(nums)-1))
        buckets = [None]*len(nums)
        for num in nums:
            i=(num-minn)//k
            if buckets[i]: buckets[i].append(num)
            else: buckets[i]=[num]
        pre,re = max(buckets[0]),float("-inf")
        for i in range(1, len(nums)):
            if not buckets[i]: continue
            maxx,minn = max(buckets[i]),min(buckets[i])
            re, pre = max(re, minn-pre), maxx
        return re

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.maximumGap([3,6,9,1]),3)
    test(sol.maximumGap([10]),0)
    x = [1,2,3,4,5]
    shuffle(x)
    test(sol.maximumGap(x),1)
    test(sol.maximumGap([1,1,1,1]),0)   #6

# Accepted
# 40/40 cases passed (1092 ms)
# Your runtime beats 73.49 % of python3 submissions
# Your memory usage beats 36.87 % of python3 submissions (30.1 MB)
