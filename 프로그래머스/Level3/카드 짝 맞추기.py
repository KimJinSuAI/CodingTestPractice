from itertools import permutations
def solution(board, r, c):
    answer = []
    card = {}
    for y in range(4):
        for x in range(4):
            if board[y][x]!=0:
                card[board[y][x]] = card.get(board[y][x], []) + [[y,x]] 
    card_list = list(permutations(card.keys(),len(card.keys())))
    for ca in card_list:
        now = [r,c]
        count = 0
        for num in ca:
            card[num].sort(key = lambda x: abs(now[0]-x[0])+abs(now[1]-x[1]))
            for twocard in [0,1]: 
                for axis in [0,1]:
                    while card[num][twocard][axis]!=now[axis]:
                        distance = abs(card[num][twocard][axis]-now[axis])
                        if distance==1:
                            now[0] = card[num][twocard][axis]
                            count+=1
                            break
                        else:
                            count+=1
                            p, m = [-1,0]
                            if now[axis] < card[num][twocard][axis]:
                                p,m = 1,3
                            while True:
                                now[axis]+=1*p
                                if now[axis]==m or board[now[0]][now[1]] != 0:
                                    break
                count+=1
        answer.append(count)

    return min(answer)

print(solution([
    [1,0,0,3],
    [2,0,0,0],
    [0,0,0,2],
    [3,0,1,0]],1,0), 14)