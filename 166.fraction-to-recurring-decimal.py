#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        r, e = list(), ''
        if numerator//denominator<0:
            r.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        while numerator>denominator and numerator!=0:
            bit = numerator//denominator
            numerator -= denominator * bit
            r.append(str(bit))
        if numerator!=0:
            visited = dict() # numerator->position map
            if len(r)==0 or r[-1]=='-':
                r.append('0')
            r.append('.')
            while numerator!=0:
                numerator *= 10
                if numerator in visited:
                    p = visited[numerator]
                    return f'{e.join(r[:p])}({e.join(r[p:])})'
                else:
                    bit = numerator//denominator
                    visited[numerator] = len(r)
                    r.append(str(bit))
                    numerator -= denominator * bit
        return e.join(r)

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.fractionToDecimal(1,2),'0.5')
    test(sol.fractionToDecimal(2,1),'2')
    test(sol.fractionToDecimal(2,3),'0.(6)')
    test(sol.fractionToDecimal(4,333),'0.(012)')
    test(sol.fractionToDecimal(1,5),'0.2')
    test(sol.fractionToDecimal(-1,5),'-0.2')
    test(sol.fractionToDecimal(-1,-5),'0.2')
    test(sol.fractionToDecimal(20,3),'6.(6)')
    test(sol.fractionToDecimal(1,333),'0.(003)') #32
    test(sol.fractionToDecimal(1,17),"0.(0588235294117647)") #33

# Accepted
# 39/39 cases passed (32 ms)
# Your runtime beats 66.4 % of python3 submissions
# Your memory usage beats 63.9 % of python3 submissions (14.4 MB)
