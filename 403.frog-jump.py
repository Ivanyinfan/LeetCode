#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#
from typing import List
# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        L = len(stones)
        steps_set = dict()
        for stone in stones:
            steps_set[stone]=set()
        steps_set[stones[0]].add(0)
        for i in range(L-1):
            for j in steps_set[stones[i]]:
                for diff in [-1,0,1]:
                    newStonePos = stones[i]+j+diff
                    if newStonePos in steps_set and newStonePos!=stones[i]:
                        steps_set[newStonePos].add(j+diff)
        return len(steps_set[stones[-1]])!=0
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.canCross([0,1,3,5,6,8,12,17]), True)
    test(sol.canCross([0,1,2,3,4,8,9,11]), False)
    test(sol.canCross([0,1]), True)
    test(sol.canCross([0,1,2,3,4,5]), True)
    test(sol.canCross([0,2]), False)
    test(sol.canCross([0,2,3,4,5]), False)

# Accepted
# 51/51 cases passed (268 ms)
# Your runtime beats 50.28 % of python3 submissions
# Your memory usage beats 87.35 % of python3 submissions (15.9 MB)
