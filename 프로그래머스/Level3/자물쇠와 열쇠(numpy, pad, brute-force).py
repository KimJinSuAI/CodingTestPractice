def rotate_90(m):  
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret
import copy
def pad(M, ty,by, lx,rx):
    m = copy.deepcopy(M)
    for i in range(len(m)):
        m[i] = [0]*lx+m[i]+[0]*rx
    tmp = [0 for _ in range(len(m[0]))]
    m = [tmp for _ in range(ty)] + m + [tmp for _ in range(by)]
    return m

def right(key, lock, zero, x, y):
    
    count = 0
    righty = len(lock)+len(key)-2-y
    if righty < 0:
        righty = 0
    rightx = len(lock[0])+len(key)-2-x
    if rightx < 0:
        rightx = 0

    k = pad(key,y,righty,x,rightx)
    for a in range(len(lock)):
        for b in range(len(lock[0])):
            if lock[a][b]==k[a+len(key)-1][b+len(key[0])-1]:
                return False
            elif lock[a][b]==0:
                if k[a+len(key)-1][b+len(key[0])-1]==1:
                    count+=1
    if count==zero:
        return True
    else: 
        return False


def solution(key, lock):
    # lock = np.pad(lock,((len(key)-1,0), (len(key[0])-1,0)) ,constant_values = 0)     

    zero = 0
    for y in range(len(lock)):
        for x in range(len(lock[0])):
            if lock[y][x]==0:
                zero += 1
                
    for _ in range(4):
        key = rotate_90(key)
        for y in range(len(lock)+len(key)-1):
            for x in range(len(lock[0])+len(key[0])-1):
                if right(key, lock, zero, x, y):
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	))
print(solution([[1,0],[1,0]],

                [[1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,0],
                [1,1,1,1,1,0],]))