#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i=j=k=0
        while len(nums)<n:
            mi,mj,mk=nums[i]*2,nums[j]*3,nums[k]*5
            nums.append(min(min(mi,mj),mk))
            if mi==nums[-1]: i+=1
            if mj==nums[-1]: j+=1
            if mk==nums[-1]: k+=1
        return nums[-1]
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.nthUglyNumber(1),1)
    test(sol.nthUglyNumber(10),12)
    test(sol.nthUglyNumber(2),2)
    test(sol.nthUglyNumber(3),3)
    test(sol.nthUglyNumber(4),4)
    test(sol.nthUglyNumber(20),36)

# Accepted
# 596/596 cases passed (168 ms)
# Your runtime beats 53.77 % of python3 submissions
# Your memory usage beats 48.6 % of python3 submissions (14.3 MB)
