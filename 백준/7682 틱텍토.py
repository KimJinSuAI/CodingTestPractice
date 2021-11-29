import sys
from collections import Counter
input = sys.stdin.readline
cond = [[[i,0],[i,1],[i,2]]for i in range(3)] + [[[0,i],[1,i],[2,i]]for i in range(3)] + [[[i,i] for i in range(3)]] + [[[2-i,i] for i in range(3)]]
answer = []
while True:
    board = input()[:-1]
    if board=="end": break
    D = Counter(board)
    
    board = [list(board[:3])]+[list(board[3:6])]+[list(board[6:])] 
    win = {'X':0,'O':0,'.':0}
    for a,b,c in cond:
        ay,ax = a;by,bx=b;cy,cx=c
        if board[ay][ax]==board[by][bx]==board[cy][cx]:
            win[board[ay][ax]]+=1
    if (D['O']>D['X'] #O가 더 많음
    or D['X']>D['O']+1 #X가 2개이상 많음
    or win['X']*win['O']>0 #X,O 둘다 승리
    or (win['X']==0 and win['O']==0 and D['.']!=0) #승자가 없는데 .이 있음
    or (win['O']!=0 and D['X']>D['O']) #O가 이겼는데 X가 1개이상 많음
    or (win['X']!=0 and D['O']>=D['X'])): #X가 이겼는데 O가 0개이상 많음
        answer.append("invalid")
    else:   
        answer.append("valid")
for ans in answer:
    print(ans)