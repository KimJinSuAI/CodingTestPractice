import sys
input = sys.stdin.readline

N = int(input()[:-1])
for idx in range(1,N+1):
    #DP[i][j] = A의 i길이까지와 B의 j길이까지로 T의 i+j길이를 만들 수 있는지 여부
    A,B,T = input()[:-1].split()
    DP = [[False]*(len(A)+1) for _ in range(len(B)+1)]
    DP[0][0] = True
    for i in range(1,len(A)+1):
        if A[i-1]!=T[i-1]:
            break
        DP[0][i] = True
    
    for j in range(1,len(B)+1):
        if B[j-1]!=T[j-1]:
            break
        DP[j][0] = True

    for i in range(1,len(B)+1):
        for j in range(1, len(A)+1):
            DP[i][j] = (DP[i][j-1] and A[j-1]==T[i+j-1]) or (DP[i-1][j] and B[i-1]==T[i+j-1])
        
    print("Data set ",end="")
    print(idx, end = "")
    if DP[-1][-1]:
        print(": yes")
    else:
        print(": no")
        

    