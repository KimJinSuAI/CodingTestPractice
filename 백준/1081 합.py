import sys
input = sys.stdin.readline

L,U = map(int,input().split())
ans = 0
digitnum_dict = {}
digitnum_dict['0'] = 0
def count_digitnum(num):
    tmp = 0
    if len(num)>5:
        return count_digitnum(num[:len(num)//2]) + count_digitnum(num[len(num)//2:])

    if digitnum_dict.get(num,-1)==-1:
        digitnum_dict[num] = int(num)%10 + count_digitnum(str(int(num)//10))
    return tmp + digitnum_dict[num]

for num in range(U,L-1,-1):
    ans+=count_digitnum(str(num))

print(ans)