import sys
input = sys.stdin.readline

answer = []
n = int(input())
for i in range(n):
    j,m = map(int, input().split())
    answer.append([i+1,((j-1)//(1+m)+1)*2])
answer.sort(key = lambda x: (x[1],x[0]))
print(answer[0][0],end=' ')
print(answer[0][1])