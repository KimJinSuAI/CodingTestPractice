import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n = int(input())
index = [0 for _ in range(n+1)]
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

for idx,i in enumerate(inorder):
    index[i] = idx


def pre(Is,Ie,Ps,Pe):
    if Is>Ie or Ps>Pe: return

    now = postorder[Pe]
    print(now, end= ' ')
    
    pIdx = index[now]
    left = pIdx - Is
    right = Ie-pIdx

    pre(Is,pIdx-1,Ps,Ps+left-1)
    pre(pIdx+1,Ie,Pe-right,Pe-1)
pre(0,n-1,0,n-1)