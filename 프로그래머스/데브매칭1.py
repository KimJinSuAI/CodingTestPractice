def solution(rows, columns, connections, queries):
    board = [[set()for i in range(columns+1)] for _ in range(rows+1)]
    answer = []

    #Form Circuit
    for y1,x1,y2,x2 in connections:
        board[y1][x1].add((y2,x2))
        board[y2][x2].add((y1,x1))

    #Delete Wire
    for y1,x1,y2,x2 in queries:
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)
        cnt = 0
        for i in range(y1,y2+1):
            
            if (i,x1-1) in board[i][x1]:
                board[i][x1].remove((i,x1-1))
                board[i][x1-1].remove((i,x1))
                cnt+=1
            if (i,x2+1) in board[i][x2]:
                board[i][x2].remove((i,x2+1))
                board[i][x2+1].remove((i,x2))
                cnt+=1
            

        for i in range(x1,x2+1):
            if (y1-1,i) in board[y1][i]:
                board[y1][i].remove((y1-1,i))
                board[y1-1][i].remove((y1,i))
                cnt+=1
            if (y2+1,i) in board[y2][i]:
                board[y2][i].remove((y2+1,i))
                board[y2+1][i].remove((y2,i))
                cnt+=1
        answer.append(cnt)


    return answer

print(solution(4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2], [2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]], [[2, 2, 3, 1], [1, 2, 4, 2]]))