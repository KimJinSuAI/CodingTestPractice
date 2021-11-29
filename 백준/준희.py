from collections import deque
import sys
input = sys.stdin.readline
s = deque(input()[:-1]) 
ans = []
while s[0]==s[-1]:
    s.append(s.popleft())

cnt = 1
before = s[0]
for i in range(1,len(s)):
    if s[i]==before:
        cnt+=1
    else:
        ans.append(cnt)
        cnt = 1
        before = s[i]
ans.append(cnt)


print(sorted(ans))
