#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        start = (sx,sy)
        stack = [start]
        visited = {start}
        while stack:
            x,y = stack.pop()
            if x==tx and y==ty:
                return True
            for p in [(x+y,y),(x,x+y)]:
                if (p[0]-x)*(tx-x)<0:
                    continue
                if (p[1]-y)*(ty-y)<0:
                    continue
                if p in visited:
                    continue
                visited.add(p)
                stack.append(p)
        return False
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5), True)
    test(sol.reachingPoints(sx = 1, sy = 1, tx = 2, ty = 2), False)
    test(sol.reachingPoints(sx = 1, sy = 1, tx = 1, ty = 1), True)
    test(sol.reachingPoints(35,13,455955547,420098884), False) # 104

# TLE
