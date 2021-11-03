import sys
from collections import Counter

def solution(A):
  counter,r,f = Counter(A),0,False
  while len(counter)!=0:
    k,v = counter.popitem()
    if k[0]==k[1]:
      r, f = r + v//2*4, f or v%2
    else:
      r = r + min(v,counter.pop(k[::-1],0))*4
  if f:
    r = r + 2
  return r

from utils import test
if __name__ == "__main__":
    test(solution(["ck",'kc','ho','kc']),4)
    test(solution(['ab','hu','ba','nn']),6)
    test(solution(['so','oo','kk','od']),2)
    test(solution(['do','go','ok']),0)
    test(solution(['aa','bc','cb','aa']),8)
    test(solution(['aa','bc','cb','aa','aa']),10)
    test(solution(['aa','bc','cb','bb','bb']),10)
    test(solution(['aa','bc','cb','bb','bb','bb']),10)
    test(solution(['aa','bc','cb','bb','bb','bb','bb']),14)
