import sys
input = sys.stdin.readline
n = int(input())
arr = [0,1]
cnt = 0 

for i in range(2,n+1):
    j = 1
    mini = 4
    while j**2 <=i:
        mini = min(mini, arr[i-j**2])
        j+=1
    arr.append(mini+1)
            

print(arr[n])