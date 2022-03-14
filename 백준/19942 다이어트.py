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
for i in range(1,N+1):
    for order in list(combinations(range(N),i)): 
        now = [ 0 for _ in range(5)]
        for y in order:
            for x in range(5):
                now[x] +=arr[y][x]

        if isright(now):
            if mini>now[4]:
                mini = now[4]
                min_ord = [list(map(lambda x: x+1, order))]
            elif mini==now[4]:
                min_ord.append(list(map(lambda x: x+1, order)))
        
    
if min_ord:
    min_ord.sort()
    print(mini)
    print(*min_ord[0])
else:
    print(-1)
