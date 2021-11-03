from typing import List
from collections import defaultdict
class Solution:
    def solution(self, A:List[str]) -> int:
        map,r = defaultdict(int),0
        for s in A:
            rev = s[::-1]
            if map[rev]>0: map[rev],r=map[rev]-1,r+4
            else: map[s]=map[s]+1
        for k, v in map.items():
            if k==k[::-1] and v>0:
                r = r + 2
                break
        return r

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution(["ck",'kc','ho','kc']),4)
    test(sol.solution(['ab','hu','ba','nn']),6)
    test(sol.solution(['so','oo','kk','od']),2)
    test(sol.solution(['do','go','ok']),0)
    test(sol.solution(['aa','bc','cb','aa']),8)
    test(sol.solution(['aa','bc','cb','aa','aa']),10)
    test(sol.solution(['aa','bc','cb','bb','bb']),10)
    test(sol.solution(['aa','bc','cb','bb','bb','bb']),10)
    test(sol.solution(['aa','bc','cb','bb','bb','bb','bb']),14)
