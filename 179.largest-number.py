#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from typing import List
# @lc code=start
class Number(str):
    def __lt__(self: str, __x: str) -> bool:
        return self+__x < __x+self

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = map(lambda x:Number(x), nums)
        r = ''.join(sorted(numbers, reverse=True))
        if r[0]=='0': r = '0'
        return r
        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.largestNumber([10,2]), "210")
    test(sol.largestNumber([3,30,34,5,9]), "9534330")
    test(sol.largestNumber([1]), "1")
    test(sol.largestNumber([30]), "30")

# Accepted
# 230/230 cases passed (40 ms)
# Your runtime beats 70.39 % of python3 submissions
# Your memory usage beats 61.14 % of python3 submissions (14.2 MB)
