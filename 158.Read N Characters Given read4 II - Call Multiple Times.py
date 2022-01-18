#
# @lc app=leetcode id=158 lang=python3
#
# [158] Read N Characters Given read4 II - Call Multiple Times
#
from email import utils
from typing import List
from utils import read4
# @lc code=start
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buf4 = [None]*4
        self.i4 = 4
        self.l4 = 4

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i<n:
            if self.i4 == self.l4:
                if self.l4 != 4:
                    break
                self.l4 = read4(self.buf4)
                self.i4 = 0
                if self.l4 == 0:
                    break
            while i<n and self.i4<self.l4:
                buf[i] = self.buf4[self.i4]
                i, self.i4 = i+1, self.i4+1
        return i
        
# @lc code=end
from utils import test, read4_init
if __name__ == "__main__":
    # 2
    read4_init('abc')
    buf = [None]*100
    sol = Solution()
    num = sol.read(buf, 4)
    test(num, 3)
    test(''.join(buf[:num]), 'abc')
    num = sol.read(buf, 1)
    test(''.join(buf[:num]), '')
    # 68
    input = "WRBqHdrOkyIDsdRMwRSYLBfaCYEdgxPlrlNppfkOKcqNnuwSmbUcJISmKtXxvRBJTSFzfMfdRsfbnvhFSqWQaeCZFKlOJppRXiZx"
    read4_init(input)
    sol = Solution()
    num = sol.read(buf, 99)
    test(num, 99)
    test(''.join(buf[:num]), input[:99])
    num = sol.read(buf, 2)
    test(num, 1)
    test(''.join(buf[:num]), input[-1])
    num = sol.read(buf, 1)
    test(num, 0)
    test(''.join(buf[:num]), '')

# Success
# Details 
# Runtime: 46 ms, faster than 24.00% of Python3 online submissions for Read N Characters Given read4 II - Call Multiple Times.
# Memory Usage: 14.1 MB, less than 94.78% of Python3 online submissions for Read N Characters Given read4 II - Call Multiple Times.
