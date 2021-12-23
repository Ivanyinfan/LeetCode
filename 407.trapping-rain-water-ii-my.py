#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
from typing import List
# @lc code=start
class Solution42:
    def trap(self, height: List[int]) -> int:
        # left wall, right wall, left, right
        L = len(height)
        lw,rw,l,r,water = 0,L-1,0,L-1,[0]*L
        while l<=r:
            if height[l]>=height[lw]: lw,l = l,l+1
            elif height[r]>=height[rw]: rw,r = r, r-1
            else:
                if height[lw]<height[rw]:
                    water[l] = max(min(height[lw],height[rw])-height[l],0)
                    l = l + 1
                else:
                    water[r] = max(min(height[lw],height[rw])-height[r],0)
                    r = r - 1
        return water

class Solution:
    def __init__(self) -> None:
        self.sol = Solution42()

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m,n =  len(heightMap), len(heightMap[0])
        result = list()
        for height in heightMap:
            result.append(self.sol.trap(height))
        for j in range(n):
            height = [heightMap[i][j] for i in range(m)]
            r = self.sol.trap(height)
            for i in range(m):
                result[i][j]=min(r[i], result[i][j])
        total = 0
        for r in result:
            total+=sum(r)
        return total
# @lc code=end
from utils import test
if __name__ == "__main__":
    # sol = Solution42()
    # test(sum(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])),6)
    # test(sum(sol.trap([4,2,0,3,2,5])),9)
    # test(sum(sol.trap([4])),0)
    # test(sum(sol.trap([4,4])),0)
    # test(sum(sol.trap([5,4,1,2])),1) #177
    # test(sum(sol.trap([5,4,3,2,1])),0)
    # test(sum(sol.trap([1,2,3,4,5])),0)
    # test(sum(sol.trap([1,2,3,1,5])),2)
    # test(sum(sol.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])),83)    #185
    # test(sum(sol.trap([2,1,2])),1)

    sol = Solution()
    # test(sol.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]),4)
    # test(sol.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]),10)
    # test(sol.trapRainWater([[1]]),0)
    test(sol.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]),14) # 20

# Incorrect
