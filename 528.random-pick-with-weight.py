#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
from typing import List
import bisect
import random
# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            w[i]+=w[i-1]
        for i in range(len(w)):
            w[i]/=w[-1]

    def pickIndex(self) -> int:
        randNum = random.random()
        index = bisect.bisect_left(self.w, randNum)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end
if __name__ == "__main__":
    w = [1]
    sol = Solution(w)
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    w = [1,3]
    sol = Solution(w)
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())
    print(sol.pickIndex())

# Accepted
# 57/57 cases passed (168 ms)
# Your runtime beats 97.54 % of python3 submissions
# Your memory usage beats 68.53 % of python3 submissions (18.8 MB)
