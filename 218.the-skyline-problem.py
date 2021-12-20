#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
from typing import List
# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        return self.divide(buildings, 0, len(buildings))

    def merge(self, result, border, height):
        if not result or result[-1][0]!=border:
            result.append([border, height])
        else:
            if height!=result[-1][1]:
                result[-1][1] = max(result[-1][1], height)

    def divide(self, buildings, start, end):
        if end-start==1:
            b = buildings[start]
            return [[b[0],b[2]],[b[1],0]]
        mid = (end+start)//2
        r1 = self.divide(buildings, start, mid)
        r2 = self.divide(buildings, mid, end)
        r = list()
        i1 = i2 = 0
        left_h = right_h = current_h = 0
        border = 0
        while i1<len(r1) and i2<len(r2):
            u_i1 = u_i2 = False
            if r1[i1][0]<=r2[i2][0]:
                left_h = r1[i1][1]
                border = r1[i1][0]
                u_i1 = True
            if r1[i1][0]>=r2[i2][0]:
                right_h = r2[i2][1]
                border = r2[i2][0]
                u_i2 = True
            max_height = max(right_h, left_h)
            if max_height!=current_h:
                self.merge(r, border, max_height)
                current_h = max_height
            if u_i1: i1+=1
            if u_i2: i2+=1
            
        if i1==len(r1): i1, r1 = i2, r2
        while i1<len(r1):
            self.merge(r, r1[i1][0], r1[i1][1])
            i1+=1
        return r
                
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12]]), [[2, 10],[3,15],[7,12],[12,0]])
    test(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]), [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])
    test(sol.getSkyline([[0,2,3],[2,5,3]]), [[0,3],[5,0]])
    test(sol.getSkyline([[1,2,1],[1,2,2],[1,2,3]]),[[1,3],[2,0]])

# Accepted
# 40/40 cases passed (152 ms)
# Your runtime beats 43.76 % of python3 submissions
# Your memory usage beats 70.49 % of python3 submissions (18.9 MB)
