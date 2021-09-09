from functools import lru_cache
Cmemo = {}

@lru_cache(maxsize=None)
def comb(n,r):
    if not Cmemo.get((n,r),-1)!=-1:
        if r!=0 and n!=0:
            Cmemo[(n,r)] = comb(n-1,r-1)+comb(n-1,r)
        elif n==0 and r!=0:
            Cmemo[(n,r)] = 0
        else:
            Cmemo[(n,r)] = 1
    return Cmemo[(n,r)]

def solution(a):
    l = len(a)
    DP = [[0]*(l+1) for _ in a[0]] #DP[i][j] = i열까지 계산했을 때 j개의 짝수행을 갖는 행렬개수
    ones = [sum(os) for os in zip(*a)]#각 열의 요소들을 더하는 파이썬의 방법
    DP[0][l-ones[0]] = comb(l, ones[0])

    for i,one in enumerate(ones[1:]):#one : 열마다 가지는 1의 개수
        for even_rows in range(l+1):
            odd_rows = l - even_rows
            for add_one in range(max(0, one-odd_rows), min(one,even_rows)+1): #add_one : 짝수행에 추가할 1의 개수
                DP[i+1][even_rows+one-2*add_one] = (DP[i+1][even_rows+one-2*add_one]+comb(even_rows,add_one)*comb(odd_rows,one-add_one)*DP[i][even_rows])%(10**7+19)
    return DP[-1][-1]%(10**7+19)
print(solution([[0,1,0],[1,1,1],[1,1,0],[0,1,1]]))
print(solution([[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]))
print(solution([[1,0,0],[1,0,0]]))