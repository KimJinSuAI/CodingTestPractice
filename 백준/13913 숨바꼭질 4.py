import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
move = [0 for _ in range(100001)]
dist = [0 for _ in range(100001)]


Q = deque([n])
while Q:
    now= Q.popleft()
    if now==k:
        tmp = k
        minroute = []
        for _ in range(dist[now]+1):
            minroute.append(tmp)
            tmp = move[tmp]
        print(dist[now])
        print(' '.join(map(str,minroute[::-1])))
        break

    for i in (now+1,now-1,now*2):
        if 0<=i<=100000 and dist[i]==0:
            move[i] = now
            dist[i] = dist[now]+1
            Q.append(i)
        