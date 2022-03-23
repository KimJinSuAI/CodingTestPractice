import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

if N%2:
    print(arr[N//2])
else:
    dis = []
    for a in [arr[N//2-1], arr[N//2]]:
        cnt = 0
        for j in arr:
            cnt+=abs(a-j)
        dis.append((a,cnt))
    print(sorted(dis, key = lambda x: (x[1],x[0]))[0][0])