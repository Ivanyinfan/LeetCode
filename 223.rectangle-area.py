#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2-ax1)*(ay2-ay1)
        area2 = (bx2-bx1)*(by2-by1)
        x_start = max(ax1, bx1)
        x_end = min(ax2, bx2)
        y_start = max(ay1, by1)
        y_end = min(ay2, by2)
        common_area = max(x_end-x_start,0)*max(y_end-y_start,0)
        return area1+area2-common_area

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2),45)
    test(sol.computeArea(ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2),16)
    test(sol.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 3, by1 = -1, bx2 = 9, by2 = 2),18+24)
    test(sol.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = -9, by1 = -1, bx2 = 0, by2 = 2),45)
    test(sol.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 5),12+54)

# Accepted
# 3080/3080 cases passed (75 ms)
# Your runtime beats 15.03 % of python3 submissions
# Your memory usage beats 24.14 % of python3 submissions (14.4 MB)
