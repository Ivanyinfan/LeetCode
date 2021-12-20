#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
from utils import KMP_Get_Next
# @lc code=start
# def KMP_Get_Next(s:str, improve:bool) -> List[int]:
#     re = [None]*len(s)
#     # j: last index, the current index is j+1
#     # k: next[j], last value of next, except the improvement back
#     re[0],j,k = -1,0,-1
#     while j<len(s)-1:
#         # k==-1 nothing to back, set the back to 0, -1 if same with s[0]
#         # s[j]==s[k] match success, s[j+1]=k+1, back again if same with s[k+1]
#         if k==-1 or s[j]==s[k]:
#             j,k = j+1,k+1
#             if improve and s[j]==s[k]:
#                 re[j]=re[k]
#                 # not back k here, because original k may be useful in the furture
#             else:
#                 # because s[:k]==s[j-k:j]
#                 re[j]=k
#         else:
#             # match fail, back k
#             k = re[k]
#     return re

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        L = len(s)
        if not L: return s
        nextt = KMP_Get_Next(s, False)
        i,j = L-1,0
        while i>-1 and j<L:
            if j==-1 or s[i]==s[j]:
                i, j = i-1, j+1
            else:
                j = nextt[j]
        if j==L:
            return s
        return s[L:j-1:-1] + s
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.shortestPalindrome("aacecaaa"),"aaacecaaa")
    test(sol.shortestPalindrome(s = "abcd"),"dcbabcd")
    test(sol.shortestPalindrome(s = "a"),"a")
    test(sol.shortestPalindrome(s = "aa"),"aa")
    test(sol.shortestPalindrome(s = "aab"),"baab")
    test(sol.shortestPalindrome(s = "ab"),"bab")
    test(sol.shortestPalindrome(s = ""),"")
    
# Accepted
# 120/120 cases passed (56 ms)
# Your runtime beats 71.95 % of python3 submissions
# Your memory usage beats 27.94 % of python3 submissions (15.8 MB)
