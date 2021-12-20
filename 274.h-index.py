#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
from typing import List
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        L = len(citations)
        bit_count = [0]*(L+1)
        for citation in citations:
            bit_count[min(citation,L)]+=1
        h = L+1
        index = L+1
        count = 0
        while index>-1 and count<h:
            index-=1
            count+=bit_count[index]
            h -= 1
        return h
        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.hIndex([3,0,6,1,5]),3)
    test(sol.hIndex([1,3,1]),1)
    test(sol.hIndex([3,4,5]),3)
    test(sol.hIndex([1,2,3,4,5]),3)
    test(sol.hIndex([1]),1)
    test(sol.hIndex([0]),0) # 71

# Accepted
# 81/81 cases passed (32 ms)
# Your runtime beats 92.73 % of python3 submissions
# Your memory usage beats 36.01 % of python3 submissions (14.7 MB)
