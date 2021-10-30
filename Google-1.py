from collections import defaultdict
class Solution:
    def solution(self, s:str) -> int:
        p,map = 0, defaultdict(set)
        for i in range(0, len(s), 2):
            map[s[i+1]].add(s[i].upper())
        for v in map.values():
            if len(v)==3: p=p+1
        return p

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution("B2R5G2R2"),1)
    test(sol.solution("R8R0B5G1B8G8"),1)
