from itertools import combinations
import sys
input = sys.stdin.readline
N, M, K = list(map(int,input().split()))

arr = list(map(int, input().split()))

ans = []
maxi = 0
for order in combinations(range(K),M):
    tmp_arr = []
    for j in order:
        tmp_arr.append(arr[j])
        
    for j in range(M-1):
        tmp_arr[j] = tmp_arr[j+1]-tmp_arr[j]
    mini = min(tmp_arr)
    if mini>maxi:
        maxi = mini
        ans = order

answer = [0 for _ in range(K)]
for i in ans:
    answer[i] = 1
print(''.join(list(map(str,answer))))