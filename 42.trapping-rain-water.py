#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # left wall, right wall, left, right
        lw,rw,l,r,water = 0,len(height)-1,0,len(height)-1,0
        while l<=r:
            if height[l]>=height[lw]: lw,l = l,l+1
            elif height[r]>=height[rw]: rw,r = r, r-1
            else:
                if height[lw]<height[rw]:
                    water, l = water+max(min(height[lw],height[rw])-height[l],0), l+1
                else:
                    water, r = water+max(min(height[lw],height[rw])-height[r],0), r-1
        return water

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]),6)
    test(sol.trap([4,2,0,3,2,5]),9)
    test(sol.trap([4]),0)
    test(sol.trap([4,4]),0)
    test(sol.trap([5,4,1,2]),1) #177
    test(sol.trap([5,4,3,2,1]),0)
    test(sol.trap([1,2,3,4,5]),0)
    test(sol.trap([1,2,3,1,5]),2)
    test(sol.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]),83)    #185
    test(sol.trap([2,1,2]),1)

# Accepted
# 320/320 cases passed (72 ms)
# Your runtime beats 79.24 % of python3 submissions
# Your memory usage beats 30.54 % of python3 submissions (15.8 MB)
