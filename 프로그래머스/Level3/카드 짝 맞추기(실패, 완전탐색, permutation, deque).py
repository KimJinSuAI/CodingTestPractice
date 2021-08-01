import copy
from itertools import permutations
from collections import deque
def move(startO, endO):
    global boardCopy
    distance = []
    for how in [(0,1),(1,0)]:   #가로, 세로 중 뭐부터 움직이나
        start = startO[:]
        end = endO[:]
        d = 0
        for axis in how:
            while start[axis]!= end[axis]:
                d+=1
                tmp = abs(start[axis]-end[axis])
                if tmp==1:       #방향키는 1차이날때만
                    start[axis] = end[axis]
                else:            #2이상차이나면 ctrl
                    p, m = [-1,0]
                    if start[axis] < end[axis]:
                        p,m = 1,3
                    while True:
                        start[axis]+=1*p
                        if start[axis]==m or boardCopy[start[0]][start[1]] != 0:
                            break
        distance.append(d)
    return min(distance)

def solution(board, r, c):
    global boardCopy
    answer = []
    card = {}
    for y in range(4):
        for x in range(4):
            if board[y][x]!=0:
                card[board[y][x]] = card.get(board[y][x], []) + [[y,x]] 
    card_list = list(permutations(card.keys(),len(card.keys())))

    for cardP in card_list:
        boardCopy = copy.deepcopy(board)
        Q = deque()
        Q.append(([r,c],0))
        for num in cardP:                            #방문할 카드종류
            tmp = []
            while Q:                                 #2개카드 중 0->1, 1->0인 경우 append
                start = Q.popleft()
                tmp.append((card[num][1], 2+start[1]+move(start[0],card[num][0])+move(card[num][0],card[num][1])))
                tmp.append((card[num][0], 2+start[1]+move(start[0],card[num][1])+move(card[num][1],card[num][0])))
            boardCopy[card[num][0][0]][card[num][0][1]] = 0
            boardCopy[card[num][1][0]][card[num][1][1]] = 0
            Q+=tmp
        
        answer.append(sorted(Q, key = lambda x: x[1])[0][1])
    return min(answer)

print(solution([
    [1,0,0,3],
    [2,0,0,0],
    [0,0,0,2],
    [3,0,1,0]],1,0), 14)