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

