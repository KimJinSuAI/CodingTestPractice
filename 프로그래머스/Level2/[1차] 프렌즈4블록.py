def isFour(x,y,board):
    go = [[1,0],[0,1],[1,1]]
    for g in go:
        if board[y+g[0]][x+g[1]]!=board[y][x]:
            return False
    return True

def solution(m, n, board):
    board = list(map(list,board))
    removeSet = set()
    count = 0
    while True:
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x]!="X":
                    if isFour(x,y,board):
                        removeSet.add((y,x))
                        removeSet.add((y+1,x))
                        removeSet.add((y,x+1))
                        removeSet.add((y+1,x+1))
        if not removeSet:
            return count
        else: 
            count +=len(removeSet)
            for r in removeSet:
                board[r[0]][r[1]]="X"
            removeSet = set()

            for x in range(n):
                drop = 0
                foundX = False
                for y in range(m-1,-1,-1):
                    if board[y][x]=="X":
                        drop+=1
                        foundX = True
                    else:
                        if foundX:
                            board[y+drop][x]=board[y][x]
                            board[y][x]="X"


print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))