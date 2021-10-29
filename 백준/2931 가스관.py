import sys
from collections import deque
input = sys.stdin.readline

board = []
R,C = list(map(int,input().split()))
for _ in range(R):
    board.append(input()[:-1])


moscow = ()
for y in range(R):
    for x in range(C):
        if board[y][x] == 'M':
            moscow = [y,x]

d = [[-1,0],[1,0],[0,-1],[0,1]]
Q = deque([moscow + [0]])
visited = [[False for _ in range(C)] for i in range(R)] 
ans = [0,0]
while Q:
    y,x, dir = Q.popleft()
    if board[y][x] =='.':
        ans=[y,x]
        break
    elif not visited[y][x]:
        visited[y][x] = True
        if board[y][x] == 'M':
            for i, dd in enumerate(d):
                dy,dx = dd
                ny,nx = dy+y, dx+x
                if -1<ny<R and -1<nx<C:
                    if ((i==0 and board[ny][nx] in ['+','|', '1','4'])
                        or (i==1 and board[ny][nx] in ['+','|','2','3'])
                        or (i==2 and board[ny][nx] in ['+','-','1','2'])
                        or (i==3 and board[ny][nx] in ['+','-','3','4'])):
                        Q.append([ny,nx,i])
                        break
        elif board[y][x] == '+':
            for i, dd in enumerate(d):
                dy,dx = dd
                ny,nx = dy+y, dx+x
                Q.append([ny,nx,i])
        else:
            if board[y][x] == '|':
                tmp = 0 if dir == 0 else 1
            elif board[y][x] == '-':
                tmp = 3 if dir == 3 else 2
            elif board[y][x] == '1':
                tmp = 1 if dir == 2 else 3
            elif board[y][x] == '2':
                tmp = 3 if dir == 1 else 0
            elif board[y][x] == '3':
                tmp = 0 if dir == 3 else 2
            elif board[y][x] == '4':
                tmp = 1 if dir == 3 else 2
            dy, dx = d[tmp]
            Q.append([y+dy,x+dx,tmp])

y,x = ans
flag = [False for _ in range(4)]
for i,dd in enumerate(d):
    dy,dx = dd
    ny,nx = y+dy,x+dx
    if -1<ny<R and -1<nx<C:
        if ((i==0 and board[ny][nx] in ['+','|', '1','4'])
            or (i==1 and board[ny][nx] in ['+','|','2','3'])
            or (i==2 and board[ny][nx] in ['+','-','1','2'])
            or (i==3 and board[ny][nx] in ['+','-','3','4'])):
            flag[i] = True
        

if flag[0] and flag[1] and flag[2] and flag[3]:
    ans.append('+')
elif flag[0] and flag[1]:
    ans.append('|')
elif flag[2] and flag[3]:
    ans.append('-')
elif flag[3] and flag[1]:
    ans.append('1')
elif flag[3] and flag[0]:
    ans.append('2')
elif flag[2] and flag[0]:
    ans.append('3')
else:
    ans.append('4')
ans[0]+=1
ans[1]+=1
for a in ans:
    print(a, end=' ')
print()