#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#
from typing import List
# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefixSum = 0
        suffixSum = 0
        for i in range(k):
            prefixSum+=cardPoints[i]
        result = prefixSum
        for i in range(1,k+1):
            prefixSum -= cardPoints[k-i]
            suffixSum += cardPoints[-i]
            result = max(prefixSum+suffixSum, result)
        return result
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3), 12)
    test(sol.maxScore(cardPoints = [2,2,2], k = 2), 4)
    test(sol.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7), 55)
    test(sol.maxScore(cardPoints = [9], k = 1), 9)
    test(sol.maxScore(cardPoints = [9,8], k = 1), 9)
    test(sol.maxScore(cardPoints = [9,8], k = 2), 17)

# Accepted
# 40/40 cases passed (568 ms)
# Your runtime beats 26.03 % of python3 submissions
# Your memory usage beats 36.88 % of python3 submissions (27.7 MB)
