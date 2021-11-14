import sys

N = input()[:]
n = len(N)
nums = []
ans = [0]*10
for i in range(n+1):
    tmp = N[:i]
    tmp2 = N[i+1:]
    if tmp == '':
        tmp = 0
    if tmp2 == '':
        tmp2 = 0
    nums.append([int(tmp),int(tmp2)])


for j in range(1,n):
    if N[j]=='0':
        ans[0]+=(nums[j][0]-1)*(10**(n-j-1))+nums[j][1]+1
    else:
        ans[0]+=(nums[j][0])*(10**(n-j-1))

for i in range(1,10):
    for j in range(n):
        if int(N[j])>i:
            ans[i]+=(10**(n-j-1))*(nums[j][0]+1)
        elif int(N[j])==i:
            ans[i]+=((10**(n-j-1))*(nums[j][0])+nums[j][1]+1)
        else:
            ans[i]+=(10**(n-j-1))*(nums[j][0])
for a in ans:
    print(a, end = ' ')
print()