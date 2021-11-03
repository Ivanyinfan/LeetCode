# There is a string S consisting of N letters 'a' and 'b'.
# In one move, a single letter can be removed. Removing the first or the last letter in the string costs 1 and removing any other letter costs 2.

class Solution:
    def solution(self, S:str) -> int:
        l = len(S)
        dp1,dp2 = [None]*(l+1),[None]*(l+1)
        dp1[0] = dp2[-1] = 0
        for i in range(l):
            if S[i]=='a': dp1[i+1]=dp1[i]
            else: dp1[i+1]=min(i+1, dp1[i]+2)
        for i in range(l-1, -1, -1):
            if S[i]=='a': dp2[i]=dp2[i+1]
            else: dp2[i]=min(l-i, dp2[i+1]+2)
        r = min([dp1[i]+dp2[i] for i in range(l)])
        return r

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution('aabaa'),2)
    test(sol.solution('abbaaba'),5)
    test(sol.solution('bbb'),3)
    test(sol.solution('abbbaabaabbba'),10)
    test(sol.solution('b'),1)
    test(sol.solution('bb'),2)
    test(sol.solution('bbbbb'),5)
    test(sol.solution('aaa'),0)
    test(sol.solution('aab'),1)
    test(sol.solution('aabb'),2)
    test(sol.solution('aabbaa'),4)
    test(sol.solution('aabbbaa'),5)
    test(sol.solution('aaaaaaabaa'),2)
    test(sol.solution('aaaaaabaabbbbbbbbbbaaaaaaaaaaaaaaaaaaa'),19)
