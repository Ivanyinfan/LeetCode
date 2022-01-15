#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
from typing import List
from utils import UnionFind
# @lc code=start
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        for stone in stones:
            uf.union(stone[0], ~stone[1])
        return len(stones) - uf.getCount()
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]), 5)
    test(sol.removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]), 3)
    test(sol.removeStones(stones = [[0,0]]), 0)

# Success
# Runtime: 140 ms, faster than 95.51% of Python3 online submissions for Most Stones Removed with Same Row or Column.
# Memory Usage: 15 MB, less than 63.00% of Python3 online submissions for Most Stones Removed with Same Row or Column.
