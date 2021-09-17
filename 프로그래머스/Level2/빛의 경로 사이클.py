def go(ny,nx, dir):
    global grid, memo
    tmp = []
    count = 0
    while True:
        if ny==-1:
            ny = len(grid)-1
        elif ny==len(grid):
            ny = 0
        if nx==-1:
            nx = len(grid[0])-1
        elif nx==len(grid[0]):
            nx = 0
            
        if memo.get((ny,nx,dir),False):
            return count
        memo[(ny,nx,dir)] = True
        tmp.append((ny,nx, dir))
        count+=1

        if grid[ny][nx]=="S":
            if dir==2:#O
                ny+=1
            elif dir==6:
                nx+=1
            elif dir==4:
                nx-=1
            else:
                ny-=1
        elif grid[ny][nx]=="L":
            if dir==2:#O
                dir = 6
                nx+=1
            elif dir==8:
                dir = 4
                nx-=1
            elif dir == 6:
                dir = 8
                ny-=1
            else:
                dir = 2
                ny+=1
        elif grid[ny][nx]=="R":
            if dir==2:
                dir = 4
                nx-=1
            elif dir==8:
                dir = 6
                nx+=1
            elif dir == 6:
                dir = 2
                ny+=1
            else:
                dir = 8
                ny-=1

def solution(Grid):
    global grid, memo
    memo = {}
    grid = Grid
    answer = []
    d = [2,4,6,8]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for dir in d:
                tmp = go(y,x,dir)
                if tmp>0:
                    answer.append(tmp)
    return sorted(answer)

print(solution(["SL","LR"]))