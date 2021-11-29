from collections import deque
def solution(board, durability):
    if board[0][0] in [1,3,5]:
        return 0

    d = [[-1,0],[1,0],[0,-1],[0,1]]    #상하좌우
    cnt = 0
    Q = deque([[0,0,3]])
    while Q:
        y,x,dir = Q.popleft()
        if -1<y<len(board) and -1<x<len(board[0]):
            cnt+=1
        else:
            break
        dy,dx = d[dir]
        ny,nx = y+dy,x+dx
        if -1<ny<len(board) and -1<nx<len(board[0]):
            if board[ny][nx]==0 or durability[ny][nx]==0:
                Q.append([ny,nx,dir])
            else:
                durability[ny][nx]-=1
                if board[ny][nx]==1:
                    if dir == 0: #상
                        dir = 3
                    elif dir == 2:  #좌
                        dir = 1
                    elif dir == 1:  #하
                        cnt-=1
                        dir = 0
                    else:           #우
                        cnt-=1
                        dir = 2
                elif board[ny][nx]==2:
                    if dir == 0: #상
                        dir = 2
                    elif dir == 3:  #우
                        dir = 1
                    elif dir == 1:  #하
                        cnt-=1
                        dir = 0
                    else:           #좌
                        cnt-=1
                        dir = 3
                elif board[ny][nx]==3:
                    if dir == 0: #상
                        cnt-=1
                        dir = 1
                    elif dir == 3:  #우
                        cnt-=1
                        dir = 2
                    elif dir == 1:  #하
                        dir = 3
                    else:           #좌
                        dir = 0
                elif board[ny][nx]==4:
                    if dir == 0: #상
                        cnt-=1
                        dir = 1
                    elif dir == 3:  #우
                        dir = 0
                    elif dir == 1:  #하
                        dir = 2
                    else:           #좌
                        cnt-=1
                        dir = 3
                else:
                    cnt-=1
                    if dir == 0: #상
                        dir = 1
                    elif dir == 1:  #하
                        dir = 0
                    elif dir == 2:  #좌
                        dir = 3
                    else:           #우
                        dir = 2
                    
                Q.append([ny,nx,dir])

    return cnt
# print(solution([[0, 2, 0], [1, 0, 5], [3, 4, 0]],[[0, 2, 0], [2, 0, 1], [2, 1, 0]]))
# print(solution([[0, 2, 0], [0, 5, 0], [0, 0, 0]],[[0, 2, 0], [0, 1, 0], [0, 0, 0]]))
print(solution([[0, 0, 2, 0], [1, 0, 3, 2], [0, 0, 0, 0], [3, 0, 0, 4]], [[0, 0, 2, 0], [5, 0, 2, 5], [0, 0, 0, 0], [5, 0, 0, 5]]))

