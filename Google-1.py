from collections import defaultdict
class Solution:
    masks = {'R':1,'G':2,'B':4}
    all_mask = 1|2|4
    def solution(self, s:str) -> int:
        p,map = 0, defaultdict(int)
        for i in range(0, len(s), 2):
            map[s[i+1]]|=Solution.masks[s[i].upper()]
        for v in map.values():
            if v==Solution.all_mask: p=p+1
        return p

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.solution("B2R5G2R2"),1)
    test(sol.solution("R8R0B5G1B8G8"),1)
    test(sol.solution("R8"),0)
    test(sol.solution("G7"),0)
    test(sol.solution("B0"),0) 
    test(sol.solution("R8G8B8"),1)
    test(sol.solution("R8G8B8R8G8B8"),1)
    test(sol.solution("R8G8B8R0G0B0"),2)
    test(sol.solution("R8G8B8G0B0"),1)
    test(sol.solution("R8G8B8R0B0"),1)
    test(sol.solution("R8G8B8R0G0"),1)