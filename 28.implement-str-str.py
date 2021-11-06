#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0: return 0
        nextt = self.nextt(needle)
        i,j=0,0
        while i<len(haystack) and j<len(needle):
            if j==-1 or haystack[i]==needle[j]:
                i, j = i+1, j+1
            else:
                j = nextt[j]
        if j==len(needle):
            return i-j
        return -1

    
    def nextt(self, needle: str):
        re = [None]*len(needle)
        re[0],j,k = -1,0,-1
        while j<len(needle)-1:
            if k==-1 or needle[j]==needle[k]:
                j,k = j+1,k+1
                if needle[j]==needle[k]:
                    re[j]=re[k]
                else:
                    re[j]=k
            else:
                k = re[k]
        return re

        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.strStr('hello','ll'),2)
    test(sol.strStr('aaaaa','bba'),-1)
    test(sol.strStr('',''),0)
    test(sol.strStr('','a'),-1)
    test(sol.strStr('aaaaaaaaaaaaab','aaaab'),9)
    test(sol.strStr('aaaaaaaaaaaaaaa','aaaa'),0)

# Accepted
# 80/80 cases passed (68 ms)
# Your runtime beats 37.02 % of python3 submissions
# Your memory usage beats 32.88 % of python3 submissions (14.5 MB)
