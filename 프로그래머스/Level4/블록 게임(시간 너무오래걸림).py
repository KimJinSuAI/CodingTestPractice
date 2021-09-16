from collections import deque
def counter(y,x,board):
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = []
    Q =deque([[y,x]])
    while Q:
        ny, nx = Q.popleft()
        if [ny,nx] in visited:
            continue
        visited.append([ny,nx])
        for dy,dx in d:
            if 0<=ny+dy<len(board) and 0<=nx+dx<len(board) and board[ny+dy][nx+dx]==board[y][x]:
                Q.append([ny+dy,nx+dx])

    visited.sort()
    tmp = [[x[0]-visited[0][0],x[1]-visited[0][1]] for x in visited]
    for i,block in enumerate(blocks):
        if tmp == block:
            checkList = []
            if i==0:
                checkList = [visited[2],visited[3]]#O
            elif i==1:
                checkList = [visited[2],visited[2]]#O
            elif i==2:
                checkList = [visited[3],visited[3]]#O
            elif i==3:
                checkList = [visited[1],visited[2]]#O
            else:
                checkList = [visited[1],visited[3]]#O
            for cy,cx in checkList:
                for ccy in range(cy-1,-1,-1):
                    if board[ccy][cx]!=0:
                        return 0
            else:
                for ny,nx in visited:
                    board[ny][nx] = 0
                return 1
    else:
        return 0

def solution(board):
    global blocks
    answer = 0
    blocks = [[[0,0,0],[1,0,0],[1,1,1]],[[0,0,1],[0,0,1],[0,1,1]],[[1,0,0],[1,0,0],[1,1,0]],
    [[0,0,0],[0,0,1],[1,1,1]],[[0,0,0],[0,1,0],[1,1,1]]]
    for i,block in enumerate(blocks):
        tmpBlock = []
        for y in range(0,3):
            for x in range(0,3):
                if block[y][x]==1:
                    tmpBlock.append([y,x])
        block = sorted(tmpBlock)
        blocks[i] = [[x[0]-block[0][0],x[1]-block[0][1]] for x in block]

    for y in range(0,len(board)):
        for x in range(0,len(board)):
            if board[y][x] !=0:
                tmpA = counter(y,x,board)
                answer+=tmpA

    return answer

print(solution([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,7,7,0,0,0,0,0,0],
    [0,0,0,7,0,0,0,0,0,0],
    [0,0,6,7,0,0,0,5,0,0],
    [0,0,6,6,6,4,5,5,5,0],
    [0,0,3,0,4,4,4,0,2,0],
    [0,0,3,3,3,1,2,2,2,0],
    [0,0,0,0,1,1,1,0,0,0]]))

print(solution([
 [0,0,0,0,0,0,0,0,0,0]
,[0,0,0,2,2,0,0,0,0,0]
,[0,0,0,2,1,0,0,0,0,0]
,[0,0,0,2,1,0,0,0,0,0]
,[0,0,0,0,1,1,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0]]),1)
print(solution([[0, 2, 0, 0], [1, 2, 0, 4], [1, 2, 2, 4], [1, 1, 4, 4]]),3)
print(solution([[0, 0, 0, 0, 0], [1, 0, 0, 2, 0], [1, 2, 2, 2, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]),2)
print(solution([[0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [3, 0, 0, 2, 0], [3, 2, 2, 2, 0], [3, 3, 0, 0, 0]]),0)
print(solution([[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 2, 0], [1, 2, 2, 2]]),0)
print(solution([[2, 2, 0, 0], [1, 2, 0, 4], [1, 2, 0, 4], [1, 1, 4, 4]]),1)
print(solution([[0, 0, 1, 1, 1], [0, 0, 0, 1, 0], [3, 0, 0, 2, 0], [3, 2, 2, 2, 0], [3, 3, 0, 0, 0]]),0)
print(solution([[2, 2, 0, 0], [1, 2, 0, 4], [1, 2, 0, 4], [1, 1, 4, 4]]),1)