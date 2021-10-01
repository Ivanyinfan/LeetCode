from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def list2ListNode(input:list)->ListNode:
    head = None
    for num in reversed(input):
        head = ListNode(num, head)
    return head

def listNode2List(head:ListNode):
    r = list()
    i = head
    while i:
        r.append(i.val)
        i = i.next
    return r

def list2TreeNode(input:list):
    if not input: return None
    r=[None]
    for i in input:
        if i==None: r.append(None)
        else: r.append(TreeNode(i))
    for i in range(1, (len(r)+1)//2):
        if r[i]==None: continue
        if 2*i<len(r): r[i].left=r[2*i]
        if 2*i+1<len(r): r[i].right=r[2*i+1]
    return r[1]

def treeNode2List(root:TreeNode):
    r,i=[None]*2,1
    r[1]=root
    while i<len(r):
        if r[i]==None:
            i+=1
            continue
        if r[i].left:
            while 2*i>=len(r): r.extend([None]*(len(r)-1))
            r[2*i]=r[i].left
        if r[i].right:
            while 2*i+1>=len(r): r.extend([None]*(len(r)-1))
            r[2*i+1]=r[i].right
        i+=1
    while r and r[-1]==None: r.pop()
    for i in range(len(r)):
        if r[i]!=None:
            r[i]=r[i].val
    return r[1:]

def treeNodes2List(roots:List[TreeNode]):
    return [treeNode2List(t) for t in roots]

def list2Node(l:list)->Node:
    if not l: return None
    r=[None]
    for i in l:
        if i==None: r.append(None)
        else: r.append(Node(i))
    for i in range(1, (len(r)+1)//2):
        if r[i]==None: continue
        if 2*i<len(r): r[i].left=r[2*i]
        if 2*i+1<len(r): r[i].right=r[2*i+1]
    return r[1]

def node2List(root:Node):
    r1=treeNode2List(root)
    i,r2=root,list()
    while i:
        t=list()
        k=i
        while k:
            t.append(k.val)
            k=k.next
        r2.append(t)
        while i and not i.left and not i.right: i=i.next
        if i: i=i.left if i.left else i.right
    return r1,r2

def test(my, ans):
    if my==ans: print(True)
    else:
        print(my, ans)
        if type(my)==list or type(my)==tuple:
            for i in range(min(len(my), len(ans))):
                if my[i]!=ans[i]:
                    print(i)
                    break

class Solution51:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(f):
            nonlocal n,p,r,c
            if f==n:
                b = [["."]*n for i in range(n)]
                for i,j in enumerate(p): b[i][j]="Q"
                b = list(map(lambda x:''.join(x), b))
                r.append(b)
                return
            for i in range(n):
                if c[i]: continue
                a,b=f-1,i+1
                while a>-1 and b<n:
                    if p[a]==b: break
                    a,b=a-1,b+1
                else:
                    a,b=f-1,i-1
                    while a>-1 and b>-1:
                        if p[a]==b: break
                        a,b=a-1,b-1
                    else:
                        p[f],c[i]=i,1
                        backtrack(f+1)
                        c[i]=None
        p,r,c = [None]*n,list(),[None]*n
        backtrack(0)
        return r
