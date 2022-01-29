#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num<10:
            return num
        numStr = list(str(num))
        l = len(numStr)
        min = 0
        max = None
        newMin = 0
        for i in range(1, l):
            if (max==None and numStr[i]>numStr[newMin]) or (max!=None and numStr[i]>=numStr[max]):
                max = i
                min = newMin
            elif numStr[i]<numStr[min]:
                newMin = i
        if max!=None and numStr[min]<numStr[max]:
            for i in range(max):
                if numStr[i]<numStr[max]:
                    numStr[i], numStr[max] = numStr[max], numStr[i]
                    break
        return int(''.join(numStr))

            
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.maximumSwap(2736), 7236)
    test(sol.maximumSwap(9973), 9973)
    test(sol.maximumSwap(3), 3)
    test(sol.maximumSwap(9), 9)
    test(sol.maximumSwap(123), 321)
    test(sol.maximumSwap(39297), 99237)
    test(sol.maximumSwap(1987), 9187)
    test(sol.maximumSwap(1213), 3211)
    test(sol.maximumSwap(98368),98863) # 106

# Accepted
# 111/111 cases passed (42 ms)
# Your runtime beats 36.95 % of python3 submissions
# Your memory usage beats 99.96 % of python3 submissions (13.9 MB)
