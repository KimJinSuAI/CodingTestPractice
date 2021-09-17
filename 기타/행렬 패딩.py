import copy
def pad(M, ty,by, lx,rx):
    m = copy.deepcopy(M)
    for i in range(len(m)):
        m[i] = [0]*lx+m[i]+[0]*rx
    tmp = [0 for _ in range(len(m[0]))]
    m = [tmp for _ in range(ty)] + m + [tmp for _ in range(by)]
    return m

print(pad([[1,1,1],[1,1,1],[1,1,1]],3,3,0,1))