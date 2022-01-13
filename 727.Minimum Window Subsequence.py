#
# @lc app=leetcode id=727 lang=python3
#
# [727] Minimum Window Subsequence
#

# @lc code=start
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        l1,l2 = len(s1), len(s2)
        if l1<l2: return ''
        start1=start2=0
        start = end = None
        while start1<l1:
            if s1[start1]==s2[start2]:
                if start2 == l2-1:
                    newEnd = start1 + 1
                    while start2>=0:
                        if s1[start1]==s2[start2]:
                            start2 -= 1
                        start1 -= 1
                    start1, start2 = start1+1, start2+1
                    if start==None or newEnd-start1<end-start:
                        start, end = start1, newEnd
                    start1 += 1
                else:
                    start1, start2 = start1+1, start2+1
            else:
                start1 += 1
        if start==None:
            return ''
        return s1[start:end]
   
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.minWindow("abcdebdde","bde"),"bcde")
    test(sol.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl",'u'),'')
    test(sol.minWindow("abcdebdde","aebdde"),"abcdebdde")
    test(sol.minWindow("a","a"),"a")
    test(sol.minWindow("ab","a"),"a")
    test(sol.minWindow("aa","a"),"a")
    test(sol.minWindow("bbbbdde","bde"),'bdde')

# Success 
# Runtime: 196 ms, faster than 65.91% of Python3 online submissions for Minimum Window Subsequence.
# Memory Usage: 14.4 MB, less than 84.36% of Python3 online submissions for Minimum Window Subsequence.
