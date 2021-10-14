from collections import deque
import copy
def rotate_90(m):  
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def findPuzzle(start,i):
    puzzle = []
    Q = deque([start])
    d = [[1,0],[0,1],[-1,0],[0,-1]]
    while Q:                                    #퍼즐BFS
        nodeY,nodeX = Q.popleft()
        if Gtable[nodeY][nodeX] in [0,i+2]:
            continue
        puzzle.append([nodeY,nodeX])
        Gtable[nodeY][nodeX] = i+2
        for dy, dx in d:
            if -1<nodeY+dy<len(Gtable) and -1<nodeX+dx<len(Gtable) and Gtable[nodeY+dy][nodeX+dx]==i+1:
                Q.append([nodeY+dy,nodeX+dx])

    return puzzle
        
def findBlank(start):
    global GgameBoard
    blank = []
    Q = deque([start])
    d = [[1,0],[0,1],[-1,0],[0,-1]]
    while Q:                                    #빈칸BFS
        nodeY,nodeX = Q.popleft()
        if GgameBoard[nodeY][nodeX] in [1, True]:
            continue
        blank.append([nodeY,nodeX])
        GgameBoard[nodeY][nodeX] = True
        for dy, dx in d:
            if -1<nodeY+dy<len(GgameBoard) and -1<nodeX+dx<len(GgameBoard) and GgameBoard[nodeY+dy][nodeX+dx]==0:
                Q.append([nodeY+dy,nodeX+dx])

    for b in blank:
        GgameBoard[b[0]][b[1]] = 0
    return blank

def isRight(puzzles, blank):                    #빈칸과 퍼즐중에 같은게 있는지 확인하고 있다면 빈칸을 1로 채움
    global Ganswer
    blankZero = copy.deepcopy(blank)                        #빈칸을 0,0을 기준으로 위치 변경
    move = [51,51]
    for p in blankZero:
        if p[0]<move[0]:
            move[0] = p[0]
        if p[1]<move[1]:
            move[1] = p[1]
    
    for index in range(len(blank)):
        blankZero[index][0] -= move[0]
        blankZero[index][1] -= move[1]

    for i,puzzle in enumerate(puzzles):
        if len(puzzle)!= len(blankZero):
            continue
        move = [51,51]#퍼즐을 0,0을 기준으로 위치 변경
        puzzleZero = copy.deepcopy(puzzle)
        for p in puzzleZero:
            if p[0]<move[0]:
                move[0] = p[0]
            if p[1]<move[1]:
                move[1] = p[1]
        for index in range(len(puzzleZero)):
            puzzleZero[index][0] -= move[0]
            puzzleZero[index][1] -= move[1]

        if sorted(blankZero, key=lambda x:(x[0],x[1])) == sorted(puzzleZero, key=lambda x:(x[0],x[1])):
            for b in blank:
                GgameBoard[b[0]][b[1]] = 1
            for p in puzzle:
                Gtable[p[0]][p[1]] = 0
            puzzles.pop(i)
            Ganswer+=len(puzzleZero)
            return True
    return False

def solution(game_board, table):
    global GgameBoard, Gtable, Ganswer
    GgameBoard = game_board
    Gtable = table
    Ganswer = 0
    for i in range(4):
        puzzles = []
        for y in range(len(Gtable)):
            for x in range(len(Gtable)):
                if Gtable[y][x]==i+1:
                    puzzles.append(findPuzzle([y,x],i))
        
        for y in range(len(GgameBoard)):
            for x in range(len(GgameBoard)):
                if GgameBoard[y][x]==0:
                    blank = findBlank([y,x])
                    isRight(puzzles, blank)
        Gtable = rotate_90(Gtable)


    return Ganswer

print(solution([
    [1,1,0,0,1,0],
    [0,0,1,0,1,0],
    [0,1,1,0,0,1],
    [1,1,0,1,1,1],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]],

[[1,0,0,1,1,0],
 [1,0,1,0,1,0],
 [0,1,1,0,1,1],
 [0,0,1,0,0,0],
 [1,1,0,1,1,0],
 [0,1,0,0,0,0]]))