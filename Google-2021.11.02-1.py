import sys
from collections import defaultdict

mask = {'R':1, 'G':2, 'B':4}
all_mask = 1|2|4

def solution(S):
  global mask, all_mask
  rod_map = defaultdict(int)
  for i in range(0,len(S),2):
    rod_map[S[i+1]]|=mask[S[i].upper()]
  r = 0
  for v in rod_map.values():
    if v==all_mask:
      r = r + 1
  return r

from utils import test
if __name__ == "__main__":
    test(solution("B2R5G2R2"),1)
    test(solution("R8R0B5G1B8G8"),1)
    test(solution("R8"),0)
    test(solution("G7"),0)
    test(solution("B0"),0) 
    test(solution("R8G8B8"),1)
    test(solution("R8G8B8R8G8B8"),1)
    test(solution("R8G8B8R0G0B0"),2)
    test(solution("R8G8B8G0B0"),1)
    test(solution("R8G8B8R0B0"),1)
    test(solution("R8G8B8R0G0"),1)
    test(solution(""),0)
    test(solution("r8g8b8R0G0"),1)