#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        all_xor = 0
        for num in nums: all_xor=all_xor^num
        right_most = -all_xor&all_xor
        x = 0
        for num in nums:
            if num&right_most==0:
                x = x^num
        return [x,all_xor^x]
        

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.singleNumber([1,2,1,3,2,5]),[3,5],False)
    test(sol.singleNumber([-1,0]),[-1,0],False)
    test(sol.singleNumber([0,1]),[1,0],False)
    test(sol.singleNumber([1,2,3,3,4,4]),[1,2],False)

# Accepted
# 32/32 cases passed (52 ms)
# Your runtime beats 94.96 % of python3 submissions
# Your memory usage beats 52.19 % of python3 submissions (15.9 MB)
