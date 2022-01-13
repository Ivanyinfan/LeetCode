from typing import List
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known_person = {0, firstPerson}
        meetings.sort(key=lambda x:x[2])
        start = 0
        L = len(meetings)
        while start<L:
            end = start+1
            while end<L and meetings[end][2]==meetings[start][2]:
                end += 1
            f = False
            for i in range(start, end):
                if meetings[i][0] in known_person or meetings[i][1] in known_person:
                    f = True
                    break
            if f:
                for i in range(start, end):
                    known_person.add(meetings[i][0])
                    known_person.add(meetings[i][1])
            start = end
        return list(known_person)

from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1), [0,1,2,3,5], False)
    test(sol.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3), [0,1,3], False)
    test(sol.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1), [0,1,2,3,4], False)
    test(sol.findAllPeople(n = 1, meetings = [[0,1,1]], firstPerson = 1), [0,1], False)
    test(sol.findAllPeople(n = 1, meetings = [[0,1,1]], firstPerson = 0), [0,1], False)
    test(sol.findAllPeople(n = 6, meetings = [[0,2,1],[1,3,1],[4,5,1]], firstPerson = 1), [0,1,2,3], False) # 34
    