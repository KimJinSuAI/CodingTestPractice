import sys
from collections import deque
input = sys.stdin.readline

visited = {}
Q = deque([])
Q.append(map(int,input().split()))

while Q:
    A,B,C = Q.popleft()
    A,B,C = sorted([A,B,C])
    if not visited.get((A,B,C),False):
        visited[(A,B,C)] = True
        if A==B==C:
            print(1)
            break
        if A!=B:
            Q.append([A*2,B-A,C])
        if A!=C:
            Q.append([A*2,B,C-A])
        if B!=C:
            Q.append([A,B*2,C-B])
else:
    print(0)

