import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    for j in map(int, input().split()):
        heapq.heappush(arr,j)
    if i!=0:
        for j in range(N):
            heapq.heappop(arr)

# arr.sort(reverse= True)
# print(arr[N-1])
#메모리초과
print(heapq.heappop(arr))
#