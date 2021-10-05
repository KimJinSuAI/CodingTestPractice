from collections import deque
import copy
memo = {}
def solution(board, aloc, bloc):
    Aanswer = []
    Banswer = []
    Q = deque()  #True == A, False == B
    Q.append([aloc, bloc, True, copy.deepcopy(board),0])
    while Q:
        a, b, turn, B, count = Q.popleft() 
        if turn:
            locy,locx = a
            cy,cx = b
        else:
            locy,locx = b
            cy,cx = a
        if B[locy][locx]==0:
            if turn:
                Banswer.append(count)
            else:
                Aanswer.append(count)
            # if answer<count:
            #     answer = count
            continue
        B[locy][locx] = 0
        
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        cango = False
        for dy,dx in dir:
            nexty, nextx = locy+dy, locx+dx
            if 0<=nexty<len(board) and 0<=nextx<len(board[0]) and B[nexty][nextx]==1:
                if not cango:
                    cango = True
                if (nexty,nextx)==(cy,cx):      #상대편발판으로 가야해..?
                    if turn:
                        Banswer.append(count+1)
                    else:
                        Aanswer.append(count+1)
                    # if answer<count+1:
                    #     answer = count+1
                    continue

                acopy = copy.deepcopy(a)
                bcopy = copy.deepcopy(b)
                if turn:                        
                    acopy = [nexty,nextx]
                else:
                    bcopy = [nexty,nextx]
                Q.append([acopy,bcopy, not turn, copy.deepcopy(B), count+1])

        if not cango :#and answer<count:      #갈수가 없엉..
            # answer = count
            
            if turn:
                Banswer.append(count)
            else:
                Aanswer.append(count)
        
    return Aanswer, Banswer
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1, 0],[1, 2]))
# print(solution(	[[1, 1, 1, 1, 1]], [0, 0], [0, 4]))