import sys
n = int(sys.stdin.readline())
b = n-1
p = 1000000

answer = [[1,0],[0,1]]

def mul(A,B):
    tmp = [tmp for tmp in zip(*B)]
    newA = [[0] *  len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            newA[i][j] = sum(a*b for a,b in zip(A[i],tmp[j]))%p
    return newA
    
def dp(A,B):
    global answer
    while B>0:
        if B%2:
            answer = mul(answer,A)
        A = mul(A,A)
        B = B//2
    return answer
print(dp([[1,1],[1,0]],b)[0][0])