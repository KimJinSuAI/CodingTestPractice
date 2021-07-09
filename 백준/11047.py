N, K = list(map(int,input().split()))
value = list()
count=0
for i in range(N):
    value.append(int(input()))
for i in range(N):
    if value[-i-1]<=K:
        tmp = int(K/value[-i-1])
        count=count+tmp
        K=K-int(value[-i-1]*tmp)
print(count)