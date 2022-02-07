#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#
from typing import List
# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        right = float('-inf')
        for interval in intervals:
            if interval[0]<right:
                return False
            right = max(right, interval[1])
        return True
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.canAttendMeetings(intervals = [[0,30],[5,10],[15,20]]), False)
    test(sol.canAttendMeetings([[7,10],[2,4]]), True)
    test(sol.canAttendMeetings([[7,10]]), True)
    test(sol.canAttendMeetings([]), True)

# 执行结果：通过
# 显示详情
# 添加备注

# 执行用时：52 ms, 在所有 Python3 提交中击败了11.60%的用户
# 内存消耗：16.8 MB, 在所有 Python3 提交中击败了13.23%的用户
# 通过测试用例：78 / 78
