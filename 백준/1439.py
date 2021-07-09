S = input()
a0=0
a1=0
for i in range(len(S)+1):
    if i==len(S)-1:
        if S[i]=='0':
            a0=a0+1
        else:
            a1=a1+1
        break
    if S[i]!=S[i+1]:
        if int(S[i])==0:
            a0=a0+1
        else:
            a1=a1+1

print(min(a0,a1))