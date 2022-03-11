import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input()[:-1])
standard = list(map(int, input().split()))
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def isright(ll):
    for i in range(4):
        if standard[i]>ll[i]:
            return False
    return True


mini = sys.maxsize
min_ord = []
for i in range(N):
    for order in list(combinations(range(N),i)):
        now = [ 0 for _ in range(5)]
        for y in order:
            for x in range(5):
                now[x] +=arr[y][x]

        if isright(now) and mini>now[4]:
            mini = now[4]
            min_ord = list(map(lambda x: x+1, order))
    
if mini!=sys.maxsize:
    print(mini)
    print(' '.join(map(str,min_ord)))
else:
    print(-1)
