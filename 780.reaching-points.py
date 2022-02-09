#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>=sx and ty>=sy:
            if tx==sx and ty==sy:
                return True
            if tx>=ty:
                k = max((tx-sx)//ty, 1)
                tx, ty = tx-k*ty, ty
            else:
                k = max((ty-sy)//tx, 1)
                tx, ty = tx, ty-k*tx
        return False
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5), True)
    test(sol.reachingPoints(sx = 1, sy = 1, tx = 2, ty = 2), False)
    test(sol.reachingPoints(sx = 1, sy = 1, tx = 1, ty = 1), True)
    test(sol.reachingPoints(35,13,455955547,420098884), False) # 104

# Accepted
# 195/195 cases passed (84 ms)
# Your runtime beats 5.43 % of python3 submissions
# Your memory usage beats 72.7 % of python3 submissions (14 MB)
