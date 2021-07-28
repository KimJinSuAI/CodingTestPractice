from collections import deque
def solution(board):
    visited = [[-1]*len(board)for _ in range(len(board))] 
    queue = deque([(0,0,0,None)]) #y,x,cost,dir
    answer = []
    while queue:
        node = queue.popleft()
        if (node[0],node[1])==(len(board)-1,len(board)-1):
            answer.append(node[2])
        if visited[node[0]][node[1]]!=-1 and visited[node[0]][node[1]]<node[2]:
            continue
        visited[node[0]][node[1]] = node[2]
        if node[3] == "ㅡ":
            costㅡ = 100
            costㅣ = 600
        elif node[3] == "ㅣ":
            costㅡ = 600
            costㅣ = 100
        else:
            costㅣ = 100
            costㅡ = 100
        if node[1]+1<len(board) and board[node[0]][node[1]+1]==0: #right
            queue.append((node[0],node[1]+1,node[2]+costㅡ,"ㅡ"))
        if node[1]-1>-1 and board[node[0]][node[1]-1]==0: #left
            queue.append((node[0],node[1]-1,node[2]+costㅡ,"ㅡ"))
        if node[0]+1<len(board) and board[node[0]+1][node[1]]==0:#down
            queue.append((node[0]+1,node[1],node[2]+costㅣ,"ㅣ"))
        if node[0]-1>-1 and board[node[0]-1][node[1]]==0:#down
            queue.append((node[0]-1,node[1],node[2]+costㅣ,"ㅣ"))
    return min(answer)


# print(solution([[0,0,0,0,0,0,0,1],
#                 [0,0,0,0,0,0,0,0],
#                 [0,0,0,0,0,1,0,0],
#                 [0,0,0,0,1,0,0,0],
#                 [0,0,0,1,0,0,0,1],
#                 [0,0,1,0,0,0,1,0],
#                 [0,1,0,0,0,1,0,0],
#                 [1,0,0,0,0,0,0,0]]))

print(solution(	
    [[0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 1, 0, 1],
     [1, 0, 0, 0]]))