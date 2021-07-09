count = 0
one = 0
for i in range(8):
    a=list(input())
    for j in range(0,8-one,2):
        if a[j+one]=='F':
            count+=1
    one=(one+1)%2
print(count)