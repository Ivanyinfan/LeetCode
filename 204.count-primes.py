#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        visited = set()
        count = max(0, n - 2)
        maxx = int(n**0.5+1)
        for i in range(2, maxx):
            if i not in visited:
                for j in range(i*i, n, i):
                    if j not in visited:
                        visited.add(j)
                        count -= 1
        return count
                   
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
# 66/66 cases passed (8148 ms)
# Your runtime beats 10.49 % of python3 submissions
# Your memory usage beats 10.75 % of python3 submissions (323.9 MB)
