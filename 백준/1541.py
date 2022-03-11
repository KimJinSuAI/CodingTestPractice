import sys
import re
input = sys.stdin.readline
exp = input()[:-1]
nums = list(map(int,re.findall('[0-9]+',exp)))
ops = re.findall('[^0-9]+',exp)

ans = sys.maxsize
stck = [nums[0]]
for i in range(len(ops)):
    if ops[i]=='+':
        stck.append(stck.pop()+nums[i+1])
    else:
        stck.append(nums[i+1])
while len(stck)!=1:
    stck.append(-stck.pop()-stck.pop())

print(-stck[0])