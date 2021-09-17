def solution(board, skill):
    answer = 0
    nboard = [[]*len(board[0]) for _ in range(board)]
    for sk in skill:
        typ,r1,c1,r2,c2,degree = sk #r==y
        c2c1 = c2+1-c1
        if typ==1:
            degree*=-1
        
        for y in range(r1,r2+1):
            if not nboard[y][c1]:
                nboard[y][c1].append([degree,c2c1])
            else:
                tmp = []
                for i,spell in enumerate(nboard[y][c1]):
                    if spell[1]>c2c1:
                        nboard[y][c1] = [tmp+[spell[0]+degree, c2c1]+[spell[0], spell[1]-c2c1]+nboard[y][c1][i+1:]]
                        break
                    elif spell[1]==c2c1:
                        nboard[y][c1] = [tmp+[spell[0]+degree, spell[1]]+nboard[y][c1][i+1:]]
                    else:
                        tmp.append(spell[0]+degree,spell[1])


    for y in range(len(nboard)-1,-1,-1):
        for x in range(len(nboard[0])-1,-1,-1):
            



        for y in range(r1,r2+1):
            for x in range(c1,c2+1):
                board[y][x]+=degree
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]>0:
                answer+=1
    return answer
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
#0,0 3,4 -4 - 2,0 2,3 -2 - 1,0 3,1 +2 - 0,1 3,3 -1