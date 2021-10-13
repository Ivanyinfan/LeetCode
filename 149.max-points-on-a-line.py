#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
from utils import test
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lenn = len(points)
        if lenn<=2: return lenn
        m = 2
        for i in range(lenn-2):
            count = defaultdict(int)
            for j in range(i+1,lenn):
                xd = points[j][1]-points[i][1]
                if xd==0:
                    count[(0,0)]+=1
                else:
                    yd = points[j][0]-points[i][0]
                    if xd*yd>=0: xd,yd=abs(xd),abs(yd)
                    else: xd,yd=abs(xd),-abs(yd)
                    gcd = self.GCD(abs(yd),xd)
                    count[(yd//gcd,xd//gcd)]+=1
            m = max(max(count.values())+1,m)
        return m
    
    def GCD(self, a, b):
        if a<b: a,b=b,a
        while b: a,b=b,a%b
        return a

# @lc code=end
if __name__ == "__main__":
    sol = Solution()
    test(sol.maxPoints([[1,1]]),1)
    test(sol.maxPoints([[1,1],[2,2]]),2)
    test(sol.maxPoints([[1,1],[2,2],[3,3]]),3)
    test(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]),4)

# Accepted
# 34/34 cases passed (36 ms)
# Your runtime beats 99.25 % of python3 submissions
# Your memory usage beats 45.03 % of python3 submissions (14.4 MB)
