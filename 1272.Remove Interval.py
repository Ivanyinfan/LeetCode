#
# @lc app=leetcode id=1272 lang=python3
#
# [1272] Remove Interval
#
from typing import List
# @lc code=start
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = list()
        for i in intervals:
            if i[0]>=toBeRemoved[1] or i[1]<=toBeRemoved[0]:
                result.append(i)
            else:
                if i[0]<toBeRemoved[0]:
                    result.append([i[0], toBeRemoved[0]])
                if i[1]>toBeRemoved[1]:
                    result.append([toBeRemoved[1], i[1]])
        return result
            
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.removeInterval(intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]), [[0,1],[6,7]])
    test(sol.removeInterval(intervals = [[0,5]], toBeRemoved = [2,3]), [[0,2],[3,5]])
    test(sol.removeInterval(intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]), [[-5,-4],[-3,-2],[4,5],[8,9]])
    test(sol.removeInterval(intervals = [[1,2]], toBeRemoved = [0,3]), [])
    test(sol.removeInterval(intervals = [[1,2]], toBeRemoved = [1.5,3]), [[1,1.5]])
    test(sol.removeInterval(intervals = [[1,2]], toBeRemoved = [0,1.5]), [[1.5,2]])
    test(sol.removeInterval(intervals = [[1,2]], toBeRemoved = [1.2,1.3]), [[1,1.2],[1.3,2]])

# Success
# Runtime: 647 ms, faster than 6.88% of Python3 online submissions for Remove Interval.
# Memory Usage: 20.1 MB, less than 86.98% of Python3 online submissions for Remove Interval.
