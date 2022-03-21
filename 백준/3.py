from itertools import combinations
from copy import deepcopy

def swap(copy_b, i,j):
    set_ij = set([i,j])
    for y in range(len(copy_b)):
        if y not in set_ij:
            tmp = copy_b[y][i]
            copy_b[y][i] = copy_b[y][j]
            copy_b[y][j] = tmp
    for x in range(len(copy_b)):
        if x not in set_ij:
            tmp = copy_b[i][x]
            copy_b[i][x] = copy_b[j][x]
            copy_b[j][x] = tmp

def count_diff(a, copy_b):
    tmp = 0
    for y,x in a:
        y-=1
        x-=1
        if copy_b[y][x]!=1:
            tmp+=1
    return tmp

def solution(a, b, m):
    a = set(map(lambda x: tuple(sorted(x)),a))
    b = set(map(lambda x: tuple(sorted(x)),b))
    answer = 9999999
    A = [[0 for _ in range(1+len(a))] for _ in range(1+len(a))]
    B = [ [0 for _ in range(1+len(a))] for _ in range(1+len(a))]
    for n1,n2 in a:
        n1-=1
        n2-=1
        A[n1][n2] = 1
        A[n2][n1] = 1
    for n1,n2 in b:
        n1-=1
        n2-=1
        B[n1][n2] = 1
        B[n2][n1] = 1

    comb_list = list(combinations(range(1,1+len(A)),2))
    for i in range(m+1):  #바꾼 횟수
        for change_list in combinations(comb_list, i): #조합
            copy_B = deepcopy(B)
            for c1, c2 in change_list:
                swap(copy_B,c1-1,c2-1)
            answer = min(answer, count_diff(a,copy_B))

    
    
# while A!=B:
    return answer

print(solution([[1, 2], [2, 3]],[[1, 3], [3, 2]],1))
print(solution([[1, 2], [3, 1], [2, 4], [3, 5]], [[2, 1], [4, 1], [2, 5], [3, 2]], 1))
print(solution(
[[3, 4], [7, 2], [5, 4], [2, 3], [6, 5], [1, 2]], [[2, 1], [3, 6], [1, 4], [1, 5], [7, 1], [3, 2]], 2))