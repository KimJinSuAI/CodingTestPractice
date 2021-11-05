import sys
input = sys.stdin.readline

U,N = map(int,input().split())
arr = {}

for i in range(N):
    tmp = input().split()
    tmp[1] = int(tmp[1])
    arr[tmp[1]] = arr.get(tmp[1],[]) + [tmp[0]]

arr = sorted(arr.items(), key = lambda x: (len(x[1]),x[0]))
print(arr[0][1][0], end= ' ')
print(arr[0][0])
