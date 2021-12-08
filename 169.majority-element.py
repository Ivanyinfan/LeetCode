#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pre, count = None, 0
        for num in nums:
            if pre == None:
                pre = num
                count = 1
            else:
                if num == pre:
                    count+=1
                else:
                    count-=1
                    if count == 0:
                        pre = None
        return pre
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.majorityElement([3,2,3]),3)
    test(sol.majorityElement([2,2,1,1,1,2,2]),2)
    test(sol.majorityElement([3]),3)
    test(sol.majorityElement([2,3,3,3]),3)
    test(sol.majorityElement([2,3,3,3,2]),3)

# Accepted
# 47/47 cases passed (164 ms)
# Your runtime beats 78.96 % of python3 submissions
# Your memory usage beats 11.54 % of python3 submissions (15.6 MB)
