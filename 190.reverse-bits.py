#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        n = n>>16 | n<<16
        n = (n&0xff00ff00)>>8 | (n&0x00ff00ff)<<8
        n = (n&0xf0f0f0f0)>>4 | (n&0x0f0f0f0f)<<4
        # 1100 -> C and 0011 -> 3
        n = (n&0xcccccccc)>>2 | (n&0x33333333)<<2
        # 1010 -> A and 0101 -> 5
        n = (n&0xaaaaaaaa)>>1 | (n&0x55555555)<<1
        return n

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.reverseBits(0b00000010100101000001111010011100), 964176192)
    test(sol.reverseBits(0b11111111111111111111111111111101), 3221225471)

# Accepted
# 600/600 cases passed (20 ms)
# Your runtime beats 99.51 % of python3 submissions
# Your memory usage beats 97.65 % of python3 submissions (14 MB)
