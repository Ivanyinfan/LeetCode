#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.up_map = defaultdict(list)
        self.down_map = defaultdict(list)
        for i in range(12):
            bit_num = self.countBit(i)
            self.up_map[bit_num].append(i)
            self.down_map[bit_num].append(i)
        for i in range(12,60):
            self.down_map[self.countBit(i)].append(i)

    def countBit(self, num):
        c = 0
        while num!=0:
            c, num = c+1, num&(num-1)
        return c

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        r = list()
        if turnedOn>8: return r
        for i in range(min(4,turnedOn+1)):
            up = self.up_map[i]
            down = self.down_map[turnedOn-i]
            for u in up:
                for d in down:
                    r.append(f'{u}:{d:02d}')
        return r
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.readBinaryWatch(1), ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"], False)
    a2 = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
    test(sol.readBinaryWatch(2), a2, False)
    a8 = ["7:31","7:47","7:55","7:59","11:31","11:47","11:55","11:59"]
    test(sol.readBinaryWatch(8), a8, False)

# Accepted
# 11/11 cases passed (28 ms)
# Your runtime beats 92.59 % of python3 submissions
# Your memory usage beats 95.74 % of python3 submissions (14.1 MB)
