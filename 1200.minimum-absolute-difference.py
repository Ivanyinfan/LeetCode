#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn = arr[1]-arr[0]
        count = defaultdict(list)
        for i in range(1, len(arr)):
            d = arr[i]-arr[i-1]
            if d>minn: continue
            count[d].append([arr[i-1],arr[i]])
            minn = min(minn, d)
        return count[minn]
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minimumAbsDifference([4,2,1,3]),[[1,2],[2,3],[3,4]])
    test(sol.minimumAbsDifference([1,3,6,10,15]),[[1,3]])
    test(sol.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]),[[-14,-10],[19,23],[23,27]])

# Accepted
# 36/36 cases passed (328 ms)
# Your runtime beats 87.98 % of python3 submissions
# Your memory usage beats 99.41 % of python3 submissions (27.9 MB)
