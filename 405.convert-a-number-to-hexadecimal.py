#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.num_map = dict()
        for i in range(10):
            self.num_map[i]=str(i)
        self.num_map[10]='a'
        self.num_map[11]='b'
        self.num_map[12]='c'
        self.num_map[13]='d'
        self.num_map[14]='e'
        self.num_map[15]='f'

    def toHex(self, num: int) -> str:
        mask = 0xf0000000
        right = 28
        r = list()
        while mask!=0:
            tmp = (num&mask)>>right
            if r or tmp!=0:
                r.append(self.num_map[tmp])
            mask=mask>>4
            right-=4
        if len(r)==0:
            return '0'
        return ''.join(r)


# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.toHex(26),'1a')
    test(sol.toHex(-1),'ffffffff')
    test(sol.toHex(1),'1')
    test(sol.toHex(0),'0')
    test(sol.toHex(452345),"6e6f9")

# Accepted
# 100/100 cases passed (32 ms)
# Your runtime beats 56.01 % of python3 submissions
# Your memory usage beats 39.31 % of python3 submissions (14.3 MB)
