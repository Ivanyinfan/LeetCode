#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        indexs = [1,1,1]
        current_val = [2,3,5]
        factor = [2,3,5]
        i = 1
        while i<n:
            minn = min(current_val)
            index = current_val.index(minn)
            if minn>nums[-1]:
                nums.append(minn)
                i+=1
            current_val[index]=nums[indexs[index]]*factor[index]
            indexs[index]+=1
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
# 596/596 cases passed (248 ms)
# Your runtime beats 26.28 % of python3 submissions
# Your memory usage beats 48.6 % of python3 submissions (14.3 MB)
