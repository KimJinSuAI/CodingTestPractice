import sys
input = sys.stdin.readline

def push(y,x):
    global d,tmp
    for dy,dx in d:
        ny,nx = y+dy,x+dx
        if -1<ny<10 and -1<nx<10:
            tmp[ny][nx] = (tmp[ny][nx]+1)%2

d = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
board = [[] for _ in range(10)]
for i in range(10):
    tmp = input().strip()
    for j,ch in enumerate(tmp):
        if ch=='O':
            board[i].append(1)
        else:
            board[i].append(0)

ans = 101
for i in range(1<<10):
    tmp = []
    cnt = 0
    for j in range(10):
        tmp.append(board[j][:])
    
    for j in range(10):
        if i & 1<<j:
            push(0,j)
            cnt+=1

    for y in range(1,10):
        for x in range(10):
            if tmp[y-1][x]:
                push(y,x)
                cnt+=1

    if sum(tmp[9])==0:
        ans = min(ans,cnt)
print(ans if ans!= 101 else -1)

