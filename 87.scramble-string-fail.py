#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
primes = [2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        L = len(s1)
        self.s1 = s1
        self.s2 = s2
        ns1, ns2 = [None]*(L+1), [None]*(L+1)
        ns1[0]=ns2[0]=1
        for i in range(L):
            ns1[i+1]=ns1[i]*primes[ord(s1[i])-ord('a')]
            ns2[i+1]=ns2[i]*primes[ord(s2[i])-ord('a')]
        return self.isScramble2(ns1, ns2, 1, L, 1, L)

    def isScramble2(self, ns1, ns2, start1, end1, start2, end2):
        if start1>end1 or start2>end2: return True
        if ns2[end2]//ns2[start2-1]!=ns1[end1]//ns1[start1-1]: return False
        for i in range(start1, end1+1):
            if self.s1[i-1]!=self.s2[start2+(i-start1)-1]: break
        else:
            return True
        if i!=start1:
            return self.isScramble2(ns1, ns2, i, end1, start2+i-start1, end2)
        # for i in range(start1, end1+1):
        #     if self.s1[i-1]!=self.s2[end2-(i-start1)-1]: break
        # else:
        #     return True
        # if i!=start1:
        #     return self.isScramble2(ns1, ns2, i, end1, start2, end2-(i-start1))
        for i in range(start1, end1):
            if ns1[i]//ns1[start1-1]==ns2[start2+i-start1]//ns2[start2-1]:
                l1 = self.isScramble2(ns1, ns2, start1,i,start2, start2+i-start1)
                l2 = self.isScramble2(ns1, ns2, i+1, end1, start2+i-start1+1, end2)
                return l1 and l2
        for i in range(start1, end1):
            if ns1[i]//ns1[start1-1]==ns2[end2]//ns2[end2-(i-start1)-1]:
                l1 = self.isScramble2(ns1, ns2, start1,i,end2-(i-start1), end2)
                l2 = self.isScramble2(ns1, ns2, i+1, end1, start2, end2-(i-start1)-1)
                return l1 and l2
        return False
        
# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.isScramble('great','rgeat'),True)
    test(sol.isScramble('abcde','caebd'),False)
    test(sol.isScramble('a','a'),True)
    test(sol.isScramble('great','rgtea'),True)
    test(sol.isScramble('great','rgtae'),True)
    test(sol.isScramble('great','rgaet'),True)
    test(sol.isScramble('great','eatrg'),True)
    test(sol.isScramble('great','tearg'),True)
    test(sol.isScramble('great','aetgr'),True)
    test(sol.isScramble("abcdbdacbdac","bdacabcdbdac"), True) #281
    test(sol.isScramble("abcdbdacbdac","bdacabcdacbd"), True)
    test(sol.isScramble("abcd","bdac"), False)
