from typing import List
from collections import Counter
class Solution:
    def solution(self, A:List[str]) -> int:
        counter,r,f = Counter(A),0,False
        while len(counter)!=0:
            k,v = counter.popitem()
            if k[0]==k[1]: r,f=r+v//2*2, f or v%2
            else:
                reverse = k[::-1]
                if reverse in counter:
                    r = r + min(v, counter.pop(reverse))*4
        if f: r = r + 2
        return r

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution(["ck",'kc','ho','kc']),4)
    test(sol.solution(['ab','hu','ba','nn']),6)
    test(sol.solution(['so','oo','kk','od']),2)
    test(sol.solution(['do','go','ok']),0)
