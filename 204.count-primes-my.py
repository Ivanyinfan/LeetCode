#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
import bisect

# @lc code=start
primes = [2]
start = 3
class Solution:
    def countPrimes(self, n: int) -> int:
        global primes, start
        index = bisect.bisect_left(primes, n)
        if index<len(primes): return index
        if n<= start: return len(primes)
        for i in range(start, n):
            maxx = i**0.5
            f = True
            for prime in primes:
                if prime>maxx: break
                if i%prime==0:
                    f = False
                    break
            if f:
                primes.append(i)
        start = n
        return len(primes)

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.countPrimes(10), 4)
    test(sol.countPrimes(0), 0)
    test(sol.countPrimes(1), 0)
    test(sol.countPrimes(100), 25)
    test(sol.countPrimes(2), 0) #56
    test(sol.countPrimes(3), 1)
    test(sol.countPrimes(4), 2)
    test(sol.countPrimes(10000), 1229)

# Accepted
# 66/66 cases passed (9880 ms)
# Your runtime beats 5.02 % of python3 submissions
# Your memory usage beats 99.55 % of python3 submissions (27.6 MB)
