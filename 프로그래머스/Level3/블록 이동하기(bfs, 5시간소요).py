from collections import deque
def solution(board):
    visited = {}   
    answer = []
    f = ([0,0],[0,1],0)
    queue = deque() #y,x
    queue.append(f)
    while queue:
        node = queue.popleft()
        if node[0][1]<0 or node[1][0]>len(board)-1 or node[1][1]>len(board)-1 or visited.get((str(node[0]),str(node[1])),False):
            continue
        if node[1]==[len(board)-1,len(board)-1]:
            answer.append(node[2])
        visited[(str(node[0]),str(node[1]))] = True

        if (node[1][1]+1<len(board) and
            board[node[0][0]][node[0][1]+1] == 0 and        # go right 
            board[node[1][0]][node[1][1]+1] == 0 and
            not visited.get((str([node[0][0],node[0][1]+1]), str([node[1][0],node[1][1]+1])), False)):
            queue.append(([node[0][0],node[0][1]+1], [node[1][0],node[1][1]+1], node[2]+1))

        if (node[1][1]-1>-1 and
            board[node[0][0]][node[0][1]-1] == 0 and        # go left
            board[node[1][0]][node[1][1]-1] == 0 and
            not visited.get((str([node[0][0],node[0][1]-1]), str([node[1][0],node[1][1]-1])), False)):
            queue.append(([node[0][0],node[0][1]-1], [node[1][0],node[1][1]-1], node[2]+1))

        if (node[0][0]-1>-1 and                             # go up
            board[node[0][0]-1][node[0][1]] == 0 and
            board[node[1][0]-1][node[1][1]] == 0 and
            not visited.get((str([node[0][0]-1,node[0][1]]), str([node[1][0]-1,node[1][1]])), False)):
            queue.append(([node[0][0]-1,node[0][1]],[node[1][0]-1,node[1][1]], node[2]+1))

        if (node[1][0]+1<len(board) and
            board[node[0][0]+1][node[0][1]] == 0 and        # go down
            board[node[1][0]+1][node[1][1]] == 0 and
            not visited.get((str([node[0][0]+1,node[0][1]]), str([node[1][0]+1,node[1][1]])), False)):
            queue.append(([node[0][0]+1,node[0][1]], [node[1][0]+1,node[1][1]], node[2]+1))

        if node[0][1]+1==node[1][1]:                        #가로일때
            if (node[0][0]-1>-1 and                         #위로회전
                board[node[0][0]-1][node[0][1]]==0 and board[node[1][0]-1][node[1][1]]==0):
                queue.append(([node[0][0]-1,node[0][1]],node[0], node[2]+1))
                queue.append(([node[1][0]-1,node[1][1]],node[1], node[2]+1))
            if (node[0][0]+1<len(board) and                 #아래로회전
                board[node[0][0]+1][node[0][1]]==0 and board[node[1][0]+1][node[1][1]]==0):
                queue.append((node[0],[node[0][0]+1,node[0][1]], node[2]+1))
                queue.append((node[1],[node[1][0]+1,node[1][1]], node[2]+1))

        if node[0][0]+1==node[1][0]:                        #세로일때
            if (node[0][1]+1<len(board) and                  #앞으로회전
                board[node[0][0]][node[0][1]+1]==0 and board[node[1][0]][node[1][1]+1]==0):
                queue.append((node[0],[node[0][0],node[0][1]+1], node[2]+1))
                queue.append((node[1],[node[1][0],node[1][1]+1], node[2]+1))
            if (node[0][1]-1>-1 and                          #뒤로회전
                board[node[0][0]][node[0][1]-1]==0 and board[node[1][0]][node[1][1]-1]==0):
                queue.append(([node[0][0],node[0][1]-1],node[0], node[2]+1))
                queue.append(([node[1][0],node[1][1]-1],node[1], node[2]+1))
    return min(answer)

print(solution([
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]]), 7)

print(solution(
    [[0, 0, 0, 0, 1, 0],
     [0, 0, 1, 1, 1, 0],
     [0, 1, 1, 1, 1, 0],
     [0, 1, 0, 0, 1, 0], 
     [0, 0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0]]
), 10)

print(solution(
    [[0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 1, 1], 
    [0, 0, 1, 0, 0, 0, 0]]
), 21)

print(solution([
    [0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0, 0, 0]])
    , 11)

print(solution([
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 1, 1, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 1, 1, 1, 1, 1, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 0]])
    ,33)